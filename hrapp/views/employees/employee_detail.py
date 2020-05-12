import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Employee, Computer, TrainingProgram, Department
from ..connection import Connection


def create_employee(cursor, row):
    _row = sqlite3.Row(cursor, row)

    employee = Employee()
    employee.id = _row["employee_id"]
    employee.first_name = _row["first_name"]
    employee.last_name = _row["last_name"]
    employee.start_date = _row["start_date"]

    department = Department()
    department.id = _row["dept_id"]
    department.name = _row["dept_name"]
    department.budget = _row["dept_budget"]
    employee.department = department

    computer = Computer()
    computer.id = _row["comp_id"]
    computer.manufacturer = _row["computer_manufacturer"]
    computer.make = _row["computer_make"]
    computer.purchase_date = _row["comp_purchase_date"]
    computer.decommission_date = _row["comp_decommission_date"]
    employee.computer = computer

    employee.training_programs = []

    training_program = TrainingProgram()
    training_program.id = _row["training_program_id"]
    training_program.title = _row["training_program_title"]
    training_program.description = _row["training_program_description"]
    training_program.start_date = _row["training_program_start_date"]
    training_program.end_date = _row["training_program_end_date"]
    training_program.capacity = _row["training_program_capacity"]

    return (employee, department, computer, training_program)


def get_employee(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_employee
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id AS employee_id,
            e.first_name,
            e.last_name,
            e.start_date,
            d.id AS dept_id,
            d.dept_name,
            d.budget AS dept_budget,
            c.id AS comp_id,
            c.purchase_date AS comp_purchase_date,
            c.decommission_date AS comp_decommission_date,
            c.manufacturer AS computer_manufacturer,
            c.make AS computer_make,
            tp.id AS training_program_id,
            tp.title AS training_program_title,
            tp.description AS training_program_description,
            tp.start_date AS training_program_start_date,
            tp.end_date AS training_program_end_date,
            tp.capacity AS training_program_capacity
        FROM
            hrapp_employee e
            LEFT JOIN hrapp_department d ON d.id = e.department_id
            LEFT JOIN hrapp_employeecomputer ec ON e.id = ec.employee_id
            LEFT JOIN hrapp_computer c ON ec.computer_id = c.id
            LEFT JOIN hrapp_employeetrainingprogram etp ON etp.employee_id = e.id
            LEFT JOIN hrapp_trainingprogram tp ON etp.training_program_id = tp.id
        WHERE
            e.id = ?
        """, (employee_id,))

    employee_data = db_cursor.fetchall()

    employee_with_programs = {}

    for (employee, department, computer, training_program) in employee_data:

        if employee.id not in employee_with_programs:
            employee_with_programs[employee.id] = employee
            employee_with_programs[employee.id].training_programs.append(training_program)

        else:
            employee_with_programs[employee.id].training_programs.append(training_program)

    return employee_with_programs[employee_id]


def employee_detail(request, employee_id):
    if request.method == 'GET':
        employee = get_employee(employee_id)
        template_name = 'employees/employee_details.html'
        return render(request, template_name, {'employee': employee})

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE hrapp_employee
                SET last_name = ?,
                    department_id = ?
                WHERE id = ?
                """,
                (
                    form_data['last_name'], form_data["department"], employee_id,
                ))

                db_cursor.execute("""
                UPDATE hrapp_employeecomputer
                SET computer_id = ?
                WHERE employee_id = ?
                """,
                (
                    form_data['computer'], employee_id,
                ))

            return redirect(reverse('hrapp:employees'))

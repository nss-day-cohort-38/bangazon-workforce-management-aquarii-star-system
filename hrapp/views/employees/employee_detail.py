import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Employee, Computer, Department
from ..connection import Connection


def create_employee(cursor, row):
    _row = sqlite3.Row(cursor, row)

    employee = Employee()
    employee.id = _row["employee_id"]
    employee.first_name = _row["first_name"]
    employee.last_name = _row["last_name"]
    employee.start_date = _row["start_date"]
    # employee.training_programs = _row["training_program_name"]

    department = Department()
    department.id = _row["departmentID"]
    department.name = _row["dept_name"]

    computer = Computer()
    computer.id = _row["computerID"]
    computer.name = _row["computer"]

    employee.department = department
    employee.computer = computer

    return employee


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
            e.department_id,
            d.dept_name,
            d.id AS departmentID,
            c.make AS computer,
            c.id AS computerID
        FROM hrapp_employee e
        JOIN hrapp_department d ON d.id = e.department_id
        JOIN hrapp_employeecomputer ec ON e.id = ec.employee_id
        JOIN hrapp_computer c ON ec.computer_id = c.id
        WHERE e.id = ?
        """, (employee_id,))

        return db_cursor.fetchone()


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

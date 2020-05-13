import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Employee, Computer, TrainingProgram, Department
from ..connection import Connection
from datetime import date

employee = Employee()
employee.computers = []
employee.training_programs = []

def create_employee(cursor, row):
    _row = sqlite3.Row(cursor, row)

    employee.id = _row["employee_id"]
    employee.first_name = _row["first_name"]
    employee.last_name= _row["last_name"]

    return employee

def create_employee_with_department(cursor, row):
    _row = sqlite3.Row(cursor, row)

    department = Department()
    department.id = _row["dept_id"]
    department.dept_name = _row["dept_name"]
    employee.department = department

    return department

def create_employee_computers(cursor, row):
    _row = sqlite3.Row(cursor, row)

    computer = Computer()
    computer.manufacturer = _row["comp_manufacturer"]
    computer.make = _row["comp_make"]
    computer.id = _row["comp_id"]
    employee.computer = computer
    
    return computer

def create_employee_training_programs(cursor, row):
    _row = sqlite3.Row(cursor, row)

    training_program = TrainingProgram()
    training_program.title = _row["title"]

    return training_program

def get_employee(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_employee
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id AS employee_id,
            e.first_name,
            e.last_name
        FROM
            hrapp_employee e
        WHERE
            e.id = ?
        """, (employee_id,))

    data = db_cursor.fetchone()
    
    return data

def get_employee_training_programs(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_employee_training_programs
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id AS employee_id,
            tp.title
        FROM
            hrapp_employee e
            JOIN hrapp_employeetrainingprogram etp ON etp.employee_id = e.id
            LEFT JOIN hrapp_trainingprogram tp ON etp.training_program_id = tp.id
        WHERE
            e.id = ?;
	""", (employee_id,))
    
    data = db_cursor.fetchall()
    return data

def get_employee_department(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_employee_with_department
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id AS employee_id,
            d.id AS dept_id,
            d.dept_name
        FROM
            hrapp_employee e
            LEFT JOIN hrapp_department d ON d.id = e.department_id
        WHERE
            e.id = ?;
        """, (employee_id,))

        data = db_cursor.fetchone()

        return data

def get_employee_computer(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_employee_computers
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id AS employee_id,
            c.manufacturer AS comp_manufacturer,
            c.make AS comp_make,
            c.id AS comp_id
        FROM
            hrapp_employee e
            JOIN hrapp_employeecomputer ec ON ec.employee_id = e.id
            LEFT JOIN hrapp_computer c ON c.id = ec.computer_id
        WHERE
            e.id = ?
        ORDER BY
	        ec.assign_date DESC;
        """, (employee_id, ))

        data = db_cursor.fetchone()

        return data

def employee_detail(request, employee_id):
    if request.method == 'GET':
        employee = get_employee(employee_id)
        employee_department = get_employee_department(employee_id)
        employee_computer = get_employee_computer(employee_id)
        employee_training_programs = get_employee_training_programs(employee_id)
        template_name = 'employees/employee_details.html'
        context = {
          "employee": employee,
          "department": employee_department,
          "computer": employee_computer,
          "training_programs": employee_training_programs
        }

        return render(request, template_name, context)


    elif request.method == 'POST':
        form_data = request.POST
        employee_computer = get_employee_computer(employee_id)

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

                if employee_computer is None:
                    db_cursor.execute("""
                    INSERT INTO hrapp_employeecomputer
                    (employee_id, computer_id, assign_date, unassign_date)
                    VALUES (?, ?, ?, ?)
                    """,
                    (
                        employee_id, form_data['computer'], date.today(), None
                    ))
                
                else:
                    db_cursor.execute("""
                    UPDATE hrapp_employeecomputer
                    SET computer_id = ?
                    WHERE employee_id = ?
                    """,
                    (
                        form_data['computer'], employee_id,
                    ))
                
                return redirect(reverse('hrapp:employees'))
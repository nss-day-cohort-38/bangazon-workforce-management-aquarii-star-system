import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Employee, Computer
from ..connection import Connection

def create_employee(cursor, row):
    _row = sqlite3.Row(cursor, row)

    employee = Employee()
    employee.id = _row["employee_id"]
    employee.first_name = _row["first_name"]
    employee.last_name = _row["last_name"]
    employee.start_date = _row["start_date"]
    # employee.department = _row["department_name"]
    employee.computer = _row["make"]
    # employee.training_programs = _row["training_program_name"]

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
            c.make
        FROM hrapp_employee e
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
import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from hrapp.models import Department, Employee
from ..connection import Connection


def get_department(department_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_department
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            d.id,
            d.dept_name,
            d.budget
        FROM hrapp_department d
        WHERE d.id = ?
        """, (department_id,))

        department = db_cursor.fetchone()

        return department

# @login_required
def department_details(request, department_id):
    if request.method == 'GET':
        department = get_department(department_id)

        employees = get_employees(department_id)

        template = 'departments/detail.html'
        context = {
            'department': department,
            'employees': employees
        }

        return render(request, template, context)

def create_department(cursor, row):
    _row = sqlite3.Row(cursor, row)

    department = Department()
    department.id = _row["id"]
    department.dept_name = _row["dept_name"]
    department.budget = _row["budget"]

    return department

def get_employees(department_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.first_name,
            e.last_name,
            e.start_date,
            e.is_supervisor,
            e.department_id
        FROM hrapp_employee e
        WHERE e.department_id = ?
        """, (department_id,))

        employees = db_cursor.fetchall()

        return employees





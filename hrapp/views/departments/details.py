import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Department, Employee
from ..connection import Connection
from .list import create_employee_list

def get_department(department_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            d.id,
            d.dept_name,
            d.budget,
            e.first_name,
            e.last_name
        FROM hrapp_department d
        JOIN hrapp_employee e ON d.id = e.department_id
        WHERE d.id = ?
        """, (department_id,))

        return db_cursor.fetchone()

@login_required
def department_details(request, department_id):
    if request.method == 'GET':
        department = get_department(department_id)

        # department_employees = []

        # for employee in department:
        #     department_employees.append(employee)

        template = 'departments/detail.html'
        context = {
            'department': department,
            # 'employees': department_employees
        }

        return render(request, template, context)
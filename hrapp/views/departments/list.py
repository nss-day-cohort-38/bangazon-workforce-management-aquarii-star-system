import sqlite3
from django.shortcuts import render, redirect, reverse
from hrapp.models import Department, Employee
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def department_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = create_employee_list
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
            """)

            departments = db_cursor.fetchall()

            department_groups = {}

            for (department, employee) in departments:
                if department.id not in department_groups:
                    department_groups[department.id] = department
                    department_groups[department.id].employees.append(employee)
                else:
                    department_groups[department.id].employees.append(employee)

        template = 'departments/list.html'
        context = {
            'all_departments': department_groups.values()
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_department
            (
                dept_name, budget
            )
            VALUES (?, ?)
            """,
            (form_data['dept_name'], form_data['budget']))

        return redirect(reverse('hrapp:departments'))

def create_employee_list(cursor, row):
    _row = sqlite3.Row(cursor, row)

    department = Department()
    department.id = _row["id"]
    department.dept_name = _row["dept_name"]
    department.budget = _row["budget"]

    department.employees = []

    employee = Employee()
    employee.id = _row["id"]
    employee.first_name = _row["first_name"]
    employee.last_name = _row["last_name"]

    return (department, employee,)
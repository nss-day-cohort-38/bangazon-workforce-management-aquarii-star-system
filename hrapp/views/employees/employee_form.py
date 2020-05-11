import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrapp.models import Employee, model_factory
from ..connection import Connection

def get_employee(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Employee)
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            e.id,
            e.first_name,
            e.last_name,
            e.start_date,
            e.is_supervisor
        FROM hrapp_employee e;
        WHERE e.id = ?
        """, (employee_id,))

        return db_cursor.fetchone()

def get_departments():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Departments)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            d.id,
            d.name,
            d.address
        from hrapp_departments d
        """)

        return db_cursor.fetchall()

# @login_required
def employee_form(request):
    if request.method == 'GET':
        departments = ""
        # departments = get_departments()
        template = 'employees/employee_form.html'
        context = {
            'all_departments': departments
        }

        return render(request, template, context)

# @login_required
def employee_edit_form(request, employee_id):

    if request.method == 'GET':
        employee = get_employee(employee_id)
        # departments = get_departments()
        template = 'employees/employee_form.html'
        context = {
            'employee': employee,
            # 'all_departments': departments
        }

        return render(request, template, context)
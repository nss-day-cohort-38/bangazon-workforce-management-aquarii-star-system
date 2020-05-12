import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrapp.models.modelfactory import model_factory
from hrapp.views.connection import Connection
from hrapp.models import Employee, Computer

def get_employee_computer(computer_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Computer)
        db_cursor = conn.cursor()
        
        db_cursor.execute('''
        SELECT 
            c.id AS computer_id,
            c.make,
            c.manufacturer,
            ec.employee_id,
            e.first_name,
            e.last_name
        FROM hrapp_computer c 
        JOIN hrapp_employeecomputer ec
        JOIN hrapp_employee e
        WHERE ec.computer_id = c.id;
            ''', (computer_id,))
         
        return db_cursor.fetchall()

def get_employees():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Employee)
        db_cursor = conn.cursor()

        db_cursor.execute("""
           SELECT 
                e.first_name,
                e.last_name
            FROM hrapp_employee e;               
        """)
        
        return db_cursor.fetchall()

def computer_form(request):
    if request.method == 'GET':
        employees = get_employees()
        employee_computer = get_employee_computer()
        template = 'computers/form.html'
        context = {
            'employees': employees,
            'employee_computer': employee_computer
        }
        return render(request, template, context)
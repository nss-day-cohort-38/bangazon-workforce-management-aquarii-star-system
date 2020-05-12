import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrapp.models.modelfactory import model_factory
from hrapp.views.connection import Connection
from hrapp.models.employee import Employee

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
        template = 'computers/form.html'
        context = {
            'employees': employees
        }
        return render(request, template, context)
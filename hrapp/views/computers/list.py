import sqlite3
from django.shortcuts import render, redirect, reverse
from hrapp.views.connection import Connection
from hrapp.models.computer import Computer
from django.contrib.auth.decorators import login_required
from hrapp.models.modelfactory import model_factory
from datetime import date

def computer_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Computer)
            db_cursor = conn.cursor()
            
            db_cursor.execute('''
            SELECT
                c.id,
                c.make,
                c.purchase_date,
                c.manufacturer,
                c.decommission_date,
                ec.employee_id,
                ec.computer_id,
                e.id,
                e.first_name,
                e.last_name
            FROM hrapp_computer c 
            JOIN hrapp_employee e
            JOIN hrapp_employeecomputer ec ON e.id = ec.employee_id
            WHERE ec.computer_id = c.id;
            ''')
            
            all_computers = db_cursor.fetchall()
            all_computer_keys = list(dict.fromkeys(all_computers))
            
        template = 'computers/list.html'
        context = {
            'all_computers': all_computer_keys
        }
                
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
                INSERT INTO hrapp_computer
                (
                        make,
                        purchase_date,
                        manufacturer
                )
                VALUES (?, ?, ?);
                """,
                (form_data['make'], form_data['purchase_date'],
                    form_data['manufacturer']))
                
            new_computer_id = db_cursor.lastrowid
            today = date.today()
                
            db_cursor.execute("""
                INSERT INTO hrapp_employeecomputer
                    (
                        computer_id,
                        employee_id,
                        assign_date
                    )
                VALUES (?, ?, ?);
                """, 
            (new_computer_id, form_data['employee_id'], today))
            
        return redirect(reverse('hrapp:computers'))
            
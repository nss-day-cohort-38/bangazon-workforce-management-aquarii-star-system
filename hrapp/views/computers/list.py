import sqlite3
from django.shortcuts import render, redirect, reverse
from hrapp.views.connection import Connection
from hrapp.models.computer import Computer
from django.contrib.auth.decorators import login_required
from hrapp.models.modelfactory import model_factory

@login_required
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
                c.decommission_date,
                c.manufacturer
            FROM hrapp_computer c
            ''')
            
            all_computers = db_cursor.fetchall()
            
        template = 'computers/list.html'
        context = {
            'all_computers': all_computers
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
            VALUES (?, ?, ?)
            """,
            (form_data['make'], form_data['purchase_date'],
                form_data['manufacturer']))
            
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()
            
            db_cursor.execute(
                
            )

        return redirect(reverse('hrapp:computers'))
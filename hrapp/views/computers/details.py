import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from hrapp.views.connection import Connection
from hrapp.models.modelfactory import model_factory
from hrapp.models.computer import Computer

def get_employee_computer(computer_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Computer)
        db_cursor = conn.cursor()
        
        db_cursor.execute('''
        SELECT 
            c.id,
            c.make,
            c.manufacturer
        FROM hrapp_computer c 
        LEFT JOIN hrapp_employeecomputer e
        WHERE e.computer_id = ?;
            ''', (computer_id,))
         
        return db_cursor.fetchall()

    
def get_computer(computer_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Computer)
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            c.id,
            c.make,
            c.purchase_date,
            c.decommission_date,
            c.manufacturer
        FROM hrapp_computer c
        WHERE c.id = ?
        """, (computer_id,))
        
        return db_cursor.fetchone()
# Write function to determine whether can be deleted is true or false based on connected to employee
def computer_details(request, computer_id):
    if request.method == 'GET':
        computer = get_computer(computer_id)
        employee_computer = get_employee_computer(computer_id)
        
        canDelete = False

        if len(employee_computer) is 0:
            canDelete = True
        
        template = 'computers/detail.html'
        context = {
            'computer': computer,
            'canDelete': canDelete}
        
        return render(request, template, context)
    
    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM hrapp_computer
                WHERE id = ?
                """, (computer_id,))

            return redirect(reverse('hrapp:computers'))
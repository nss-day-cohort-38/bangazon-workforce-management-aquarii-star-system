import sqlite3
from django.shortcuts import render, redirect, reverse
from hrapp.models import Department, Employee
from ..connection import Connection
from django.contrib.auth.decorators import login_required

def create_employee_list(cursor, row):
    _row = sqlite3.Row(cursor, row)

    employee = Employee()
    library.id = _row["id"]
    library.title = _row["title"]
    library.address = _row["address"]

    # Note: You are adding a blank books list to the library object
    # This list will be populated later (see below)
    library.books = []

    book = Book()
    book.id = _row["book_id"]
    book.title = _row["book_title"]
    book.author = _row["author"]
    book.isbn = _row["isbn"]
    book.year_published = _row["year_published"]

    # Return a tuple containing the library and the
    # book built from the data in the current row of
    # the data set
    return (library, book,)

@login_required
def department_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                d.id,
                d.dept_name,
                d.budget
            from hrapp_department d
            """)

            all_departments = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                department = Department()
                department.id = row['id']
                department.dept_name = row['dept_name']
                department.budget = row['budget']

                all_departments.append(department)

        template = 'departments/list.html'
        context = {
            'all_departments': all_departments
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
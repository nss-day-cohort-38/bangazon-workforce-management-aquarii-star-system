import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrapp.models import Department
from ..connection import Connection
# from django.contrib.auth.decorators import login_required

# @login_required
def department_form(request):
    if request.method == 'GET':
        template = 'departments/form.html'

        return render(request, template)

        
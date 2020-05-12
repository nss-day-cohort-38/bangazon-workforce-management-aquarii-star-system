import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrapp.models.modelfactory import model_factory
from hrapp.views.connection import Connection

def computer_form(request):
    if request.method == 'GET':
        template = 'computers/form.html'
        return render(request, template)
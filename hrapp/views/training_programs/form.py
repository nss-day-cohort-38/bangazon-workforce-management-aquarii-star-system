import sqlite3
from django.shortcuts import render

def training_program_form(request):
    if request.method == 'GET':
        template = 'training_programs/form.html'
        context = {}

        return render(request, template, context)
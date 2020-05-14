import sqlite3
from django.shortcuts import render
from .details import get_training_program
from django.contrib.auth.decorators import login_required

@login_required
def training_program_form(request):
    if request.method == 'GET':
        template = 'training_programs/form.html'
        context = {}

        return render(request, template, context)
    
@login_required
def training_program_edit_form(request, training_program_id):
    if request.method == 'GET':
        training_program = get_training_program(training_program_id)

        template = 'training_programs/form.html'
        context = {
            'training_program': training_program,
        }

        return render(request, template, context)
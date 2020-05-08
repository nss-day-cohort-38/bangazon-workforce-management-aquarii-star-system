import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import TrainingProgram
from hrapp.models import model_factory
from ..connection import Connection

def get_training_program(training_program_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(TrainingProgram)
        db_cursor = conn.cursor()

        # TODO: expand with users signed up, etc.
        db_cursor.execute("""
        SELECT
            tp.id,
            tp.title,
            tp.start_date,
            tp.end_date,
            tp.capacity
        FROM hrapp_training_program tp
        WHERE tp.id = ?;
        """, (training_program_id,))

        return db_cursor.fetchone()

def training_program_details(request, training_program_id):
    if request.method == 'GET':
        training_program = get_training_program(training_program_id)

        template = 'training_programs/detail.html'
        context = {
            'training_program': training_program
        }

        return render(request, template, context)
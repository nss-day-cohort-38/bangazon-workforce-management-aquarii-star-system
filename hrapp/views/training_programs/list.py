import sqlite3
from django.shortcuts import render
from hrapp.models import TrainingProgram
from ..connection import Connection
# Importing datetime to compare dates
from datetime import datetime

def training_program_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
              SELECT
                  tp.id,
                  tp.title,
                  tp.start_date,
                  tp.end_date,
                  tp.capacity
              FROM hrapp_training_program tp;
            """)

            all_training_programs = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                training_program = TrainingProgram()
                training_program.id = row['id']
                training_program.title = row['title']
                training_program.start_date = row['start_date']
                training_program.end_date = row['end_date']
                training_program.capacity = row['capacity']

                all_training_programs.append(training_program)

        template = 'training_programs/list.html'

        # SORTING PROGRAMS INTO PAST AND FUTURE
        future_training_programs = []
        past_training_programs = []

        for training_program in all_training_programs:
            end_date = datetime.strptime(training_program.end_date, '%Y-%m-%d')
            if end_date > datetime.today():
                future_training_programs.append(training_program)
            else:
                past_training_programs.append(training_program)

        context = {
            'past_training_programs': past_training_programs,
            'future_training_programs': future_training_programs
        }
        
        return render(request, template, context)
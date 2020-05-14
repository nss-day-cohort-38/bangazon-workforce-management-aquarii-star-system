# Bangazon Workforce Mangement HR Application

## A group project by:

Aquarii Star System:
- [Matt Reeds](https://github.com/MReeds)
- [Andrew Green](https://github.com/agreen2601)
- [Jack Parsons](https://github.com/jcksnparsons)
- [Alyssa Nycum](https://github.com/alyssanycum)
- [Keith Potempa](https://github.com/keithrpotempa)

## Technologies Used

Python
- querying data from SQLite
- converting that data into class instances
- rendering those classes with Django
- defined and importing packages

Django
- views, models, templates
- routing with urls.py
- fixtures, migrations
- utilizing built-in user authentication

## Features

The Bangazon HR App is a full-stack web app that allows a user to interact with the followig components:

### Employees 
- List, detail, and form views/templates
- List view shows all employees and the departments associated with them
- Detail view shows the computer and training programs associated with that employee
- full CRUD functionality

### Departments
- List, detail, and form views/templates
- List view displays number of employees associated with each department
- Detailed view displays a list of the employee names associated with the department
- create, read, and delete functionality

### Computers
- List, detail, and form views/templates 
- List view displays all computers and the employees associated with each computer
- full CRUD functionality
- conditional delete behavior (computers can only be deleted if they are not assigned to a user)

### Training Programs 
- detailed view displays employees associated with them
- List view sorts the programs into past and upcoming based on today's date 
- full CRUD functionality
- conditional delete/edit behavior (past events cannot be modified)

## Installation Steps:

* `git clone git@github.com:nss-day-cohort-38/bangazon-workforce-management-aquarii-star-system.git && cd $_`

* Create your OSX/Linux OS virtual environment in Terminal:

  * `python -m venv workforceenv`
  * `source ./workforceenv/bin/activate`

* Or create your Windows virtual environment in Command Line:

  * `python -m venv workforceenv`
  * `source ./workforceenv/Scripts/activate`

* Install the app's dependencies:

  * `pip install -r requirements.txt`

* Build your database from the existing models:

  * `python manage.py makemigrations hrapp`
  * `python manage.py migrate`

* Create a superuser for your local version of the app:

  * `python manage.py createsuperuser`

* Populate your database with initial data from fixtures files:

  1. `python manage.py loaddata departments`
  1. `python manage.py loaddata employees`
  1. `python manage.py loaddata computers`
  1. `python manage.py loaddata training_programs`
  1. `python manage.py loaddata employee_computers`
  1. `python manage.py loaddata employee_training_programs`

* Fire up your dev server!

  * `python manage.py runserver`
  * Open in browser: `http://127.0.0.1:8000/`


## ERD

This ERD was supplied for us to reference when creating our models.

https://dbdiagram.io/d/5eb4d41339d18f5553fedf9e

Note that the column names do not conform to the Python community standards (PEP) for naming conventions. Our models use snake_case.

# Bangazon Workforce Mangement - Aquarii Star System

## A group project by:

- [Andrew Green](https://github.com/agreen2601)
- [Jack Parsons](https://github.com/jcksnparsons)
- [Alyssa Nycum](https://github.com/alyssanycum)
- [Keith Potempa](https://github.com/keithrpotempa)

## Steps to get your project started:

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


## Official Bangazon LLC ERD

This ERD was supplied for us to reference when creating our models.

https://dbdiagram.io/d/5eb4d41339d18f5553fedf9e

Note that the column names do not conform to the Python community standards (PEP) for naming conventions. Our models use snake_case.

from django.urls import path
from django.conf.urls import include
from hrapp.views import *
from hrapp.models import *
from django.contrib.auth import login

app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('accounts/login', login, name='login'),
    
    path('employees/', employee_list, name='employees'),
    path('employees/<int:employee_id>/', employee_detail, name="employee"),
    path('employee/form', employee_form, name='employee_form'),
    path('employees/<int:employee_id>/form', employee_edit_form, name='employee_edit_form'),

    path('computers/', computer_list, name='computers'),
    path('computers/<int:computer_id>/', computer_details, name="computer"),
    path('computer/form', computer_form, name='computer_form'),

    path('departments/', department_list, name='departments'),
    path('department/form', department_form, name='department_form'),
    path('departments/<int:department_id>/', department_details, name='department'),

    path('training_programs/', training_program_list, name='training_programs'),
    path('training_program/<int:training_program_id>/', training_program_details, name='training_program'),
    path('training_program/form', training_program_form, name='training_program_form'),
]

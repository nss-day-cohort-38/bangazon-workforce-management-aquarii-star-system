from django.urls import path
from django.conf.urls import include
from hrapp import views
from .views import *
from .models import *

app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('training_programs/', training_program_list, name='training_program_list'),
    path('training_program/<int:training_program_id>/', training_program_details, name='training_program'),
    path('training_program/form', training_program_form, name='training_program_form')
]

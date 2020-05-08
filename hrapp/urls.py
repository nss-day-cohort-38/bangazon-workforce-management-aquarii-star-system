from django.urls import path
from django.conf.urls import include
from hrapp import views
from .views import *
from hrapp.models import *

app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('departments/', department_list, name='departments'),
    path('department/form', department_form, name='department_form'),
]

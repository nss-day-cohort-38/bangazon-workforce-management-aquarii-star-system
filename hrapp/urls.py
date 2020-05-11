from django.urls import path
from django.conf.urls import include
from hrapp import views
from .views import *

app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('computers/', computer_list, name='computers'),
    path('computers/<int:computer_id>/', computer_details, name="computer"),
    path('computer/form', computer_form, name='computer_form'),
    path('employees/<int:employee_id>/', employee_detail, name="employee")
]

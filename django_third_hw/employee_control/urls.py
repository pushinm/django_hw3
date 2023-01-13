from django.urls import path, include
from .views import employee, logins
urlpatterns = [
    path('', employee, name='employee_list'),
    path('logins/', logins, name='logins'),
]
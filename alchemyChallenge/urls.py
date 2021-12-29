from django.urls import path
from .views import delete_employee, home

urlpatterns = [
    path('', home, name='home'),
    path('delete/<str:identifier>', delete_employee, name='delete_employee'),
]

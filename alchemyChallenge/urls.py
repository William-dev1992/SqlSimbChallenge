from django.urls import path
from .views import (
    home,
    new_employee,
    delete_employee,
    list_team,
    new_team,
    delete_team,
    list_recommendations,
    new_recommendation,
    delete_recommendation,
    list_team_employees,
    new_team_employee
)

urlpatterns = [
    path('', home, name='home'),
    path('new_employee', new_employee, name='new_employee'),
    path('delete_employee/<str:identifier>', delete_employee, name='delete_employee'),
    path('teams', list_team, name='list_team'),
    path('new_team', new_team, name='new_team'),
    path('delete_team/<str:identifier>', delete_team, name='delete_team'),
    path('recommendations', list_recommendations, name='list_recommendations'),
    path('new_recommendation', new_recommendation, name='new_recommendation'),
    path('delete_recommendation/<str:identifier>', delete_recommendation, name='delete_recommendation'),
    path('team_employees', list_team_employees, name='list_team_employees'),
    path('new_team_employee', new_team_employee, name='new_team_employee'),
]

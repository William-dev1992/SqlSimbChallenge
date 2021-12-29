from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Employee, Team, EmployeeTeam, Recommendation
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite+pysqlite:///challenge.sqlite", connect_args={'check_same_thread': False})
Session = sessionmaker(bind=engine)
session = Session()


def home(request):
    employees = session.query(Employee)

    return render(request, 'home.html', {'employees': employees})


def delete_employee(request):
    return 'vbla'

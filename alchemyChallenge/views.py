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


# Employees related

def new_employee(request):
    name = request.GET['name']
    email = request.GET['email']
    recommended_by = request.GET['recommendedBy']

    get_employee(recommended_by)

    employee = Employee(name=name, email=email, recommendation=recommended_by)

    session.add(employee)
    session.commit()

    response = HttpResponse()

    return response


def delete_employee(request, identifier):
    get_employee(identifier)

    session.query(EmployeeTeam).filter(EmployeeTeam.employee_id == identifier).delete()
    session.query(Employee).filter(Employee.employee_id == identifier).delete()

    session.commit()

    response = HttpResponse()

    return response


def count_recommendations(request, identifier):
    get_employee(identifier)

    recommendations = {
        "count": session.query(Recommendation).filter(Recommendation.recommender_id == int(identifier)).count()
    }

    return JsonResponse(recommendations, safe=False)

# Team related


def list_team(request):
    teams = session.query(Team)

    return render(request, 'home.html', {'teams': teams})


def new_team(request):
    name = request.GET['name']

    team = Team(name=name)

    session.add(team)
    session.commit()

    response = HttpResponse()

    return response


def delete_team(request, identifier):
    get_team(identifier)

    session.query(EmployeeTeam).filter(EmployeeTeam.team_id == identifier).delete()
    session.query(Team).filter(Team.team_id == identifier).delete()

    session.commit()

    response = HttpResponse()

    return response


# Recommendation related


def list_recommendations(request):
    recommendations = session.query(Recommendation)

    return render(request, 'home.html', {'recommendations': recommendations})


def new_recommendation(request):
    recommender = request.GET['recommender']
    recommended_name = request.GET['recommendedName']
    recommended_email = request.GET['recommendedEmail']

    get_employee(recommender)

    recommendation = Recommendation(recommender_id=recommender, candidate_name=recommended_name, candidate_email=recommended_email)

    session.add(recommendation)
    session.commit()

    response = HttpResponse()

    return response


def delete_recommendation(request, identifier):
    session.query(Recommendation).filter(Recommendation.recommendation_id == identifier).delete()
    session.commit()

    response = HttpResponse()

    return response


# Team_employees related


def list_team_employees(request):
    team_employees = session.query(EmployeeTeam)

    return render(request, 'home.html', {'team_employees': team_employees})


def new_team_employee(request):
    employee_id = request.GET['employeeId']
    team_id = request.GET['teamId']

    get_employee(employee_id)
    get_team(team_id)

    team_employee = EmployeeTeam(employee_id=employee_id, team_id=team_id)

    session.add(team_employee)
    session.commit()

    response = HttpResponse()

    return response


def delete_employee_from_team(request, identifier):
    session.query(EmployeeTeam).filter(EmployeeTeam.employee_team_id == identifier).delete()

    session.commit()

    response = HttpResponse()

    return response


def get_employee(identifier):
    employee = session.query(Employee.employee_id).filter(Employee.employee_id == identifier).first()

    if not employee.employee_id:
        raise Exception


def get_team(identifier):
    team = session.query(Team.team_id).filter(Team.team_id == identifier).first()

    if not team.team_id:
        raise Exception

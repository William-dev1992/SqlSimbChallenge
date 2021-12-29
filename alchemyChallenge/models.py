from django.db import models
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create your models here.

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employee'

    employee_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    recommendation = Column(Integer)


class Team(Base):
    __tablename__ = 'team'

    team_id = Column(Integer, primary_key=True)
    name = Column(String(100))


class Recommendation(Base):
    __tablename__ = 'recommendation'

    recommendation_id = Column(Integer, primary_key=True)
    recommender_id = Column(Integer)
    candidate_name = Column(String(100))
    candidate_email = Column(String(100))


class EmployeeTeam(Base):
    __tablename__ = 'employee_team'

    employee_team_id = Column(Integer, primary_key=True)
    employee_id = Column(Integer)
    team_id = Column(Integer)

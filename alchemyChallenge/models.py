from django.db import models
from sqlalchemy import Column, Integer, String, ForeignKey, and_
from sqlalchemy.ext.declarative import declarative_base

# Create your models here.
from sqlalchemy.orm import relationship, backref

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
    employee_id = Column(Integer, ForeignKey(Employee.employee_id))
    team_id = Column(Integer, ForeignKey(Team.team_id))

    employee = relationship(
        Employee,
        foreign_keys=[employee_id],
        primaryjoin=and_(Employee.employee_id == employee_id),
        lazy="joined",
        backref=backref("employee_team", lazy="noload"),
    )

    team = relationship(
        Team,
        foreign_keys=[team_id],
        primaryjoin=and_(Team.team_id == team_id),
        lazy="joined",
        backref=backref("employee_team", lazy="noload"),
    )

from enum import unique
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class EmployeeModel(db.model):
    __tablename__ = "table"
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer(),unique = True)
    name = db.Column(db.String())
    age=db.Column(db.Integer())
    
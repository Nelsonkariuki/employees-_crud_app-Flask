from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class EmployeeModel(db.model):
    __tablename__ = "table"
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer)
    
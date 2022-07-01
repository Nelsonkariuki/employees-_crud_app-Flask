from models import EmployeeModel, db
from flask import Flask, redirect, render_template, request
app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()

app.run(host='localhost', port=5000)

@app.route('/data/create' , methods = ['GET','POST'])

def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        employee = EmployeeModel(employee_id=employee_id, name=name, age=age, position = position)
        db.session.add(employee)
        db.session.commit()
        return redirect('/data')
@app.route('/data')
def RetrieveDataList():
    employees = EmployeeModel.query.all()
    return render_template('datalist.html',employees = employees)

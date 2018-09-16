from arbor.app import db

''' 
    Модель для таблицы user
    Класс User наследует от db.Model, базового класса для всех моделей из Flask-SQLAlchemy. 
'''
'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

'''
class Employee(db.Model):
    idEmployee=db.Column(db.Integer, primary_key=True)
    surname=db.Column(db.String(60),index=True)
    name = db.Column(db.String(60), index=True)
    login_KS = db.Column(db.String(60), index=True)
    phoneNumber = db.Column(db.String(12), index=True)
    employeeIdOffice = db.Column(db.Integer )
    employeeIdroles = db.Column(db.Integer)
    login = db.Column(db.String(30), index=True, unique=True)
    password = db.Column(db.String(128), index=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.login)
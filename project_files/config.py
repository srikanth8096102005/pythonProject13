from flask import Flask

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']= 'srikanthchinthapally42@gmail.com'
app.config['MAIL_PASSWORD']='Sree@566'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///flask.db'
db =SQLAlchemy(app)
app.app_context().push()
class signup_data(db.Model):
    user_id = db.Column(db.Integer,primary_key= True)
    fname =db.Column(db.String(30))
    lname = db.Column(db.String(30))
    date = db.Column(db.String(15))
    email = db.Column(db.String(50))
    password = db.Column(db.String(15), nullable=True)

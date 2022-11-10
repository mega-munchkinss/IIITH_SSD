from flask import Flask
from flask import request
from flask import session
from flask import Response
from flask_login import (LoginManager,login_manager,login_user,logout_user,login_required,UserMixin)
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///user.db'
app.config['SECRET_KEY']='secret_key'
db=SQLAlchemy(app)
login_manager=LoginManager()

login_manager.init_app(app)


class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(80),nullable=False)
    email=db.Column(db.String(80),nullable=False,unique=True)
    password=db.Column(db.String(80),nullable=False)
class Seats(UserMixin,db.Model):
    seat=db.Column(db.String(80),primary_key=True,nullable=False,unique=True)
    status=db.Column(db.String(80),nullable=False,default='AVAILABLE')
    customer=db.Column(db.String(80),nullable=True)
    price=db.Column(db.Integer,nullable=False,default=100)
with app.app_context():
    db.create_all()
    """ for i in range(10):
        seat=Seats(seat='A'+str(i),status='AVAILABLE')
        db.session.add(seat)
        db.session.commit() """
@app.route("/user/signup",methods=["POST"])
def signup():
    req=request.get_json()
    name=req['name']
    email=req['email']
    password=req['password']
    user=User(name=name,email=email,password=password)
    user_e=User.query.get(email)
    if(user_e!=None):
        return Response ("{'message':'User Exist'}",status=500)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    session['name']=name
    session['email']=email
    session['password']=password
    return Response ("{'message':'User Created Successfully'}",status=200)
    
@app.route("/user/signin",methods=["POST"])
def signin():
    req=request.get_json()
    email=req['email']
    password=req['password']
    user_e=User.query.get(email)
    if(user_e==None):
        return Response ("{'message':'User Not found'}",status=500)
    elif(user_e.password!=password):
        
        return Response ("{'message':'Invalid password'}",status=401)
    else:
        login_user(user_e)
        session['name']=user_e.name
        session['email']=email
        session['password']=password
        return Response ("{'message':'Login Successfully'}",status=200)


@app.route("/user/signout",methods=["GET"])
@login_required
def signout():
    
        logout_user()
        session['name']=''
        session['email']=''
        session['password']=''
        return Response ("{'message':'Logout Successfully'}",status=200)




@app.route("/seats/available",methods=["GET"])
@login_required
def seats_available():
    seat=Seats.query.all()
    resp={}
    print(seat)
    
    return {'seats': "nsjkn"},200


if "__main__"==__name__ :
    app.run(host="127.0.0.1",port=5000,debug=True)

from flask_app import app
from flask import Flask,render_template,redirect,request,session
from flask_app.models.user_model import User
@app.route('/')
def form():
    users=User.get_all()
    return render_template("read.html",users=users)

@app.route('/create')
def create():
    return render_template("create.html")

@app.route('/process',methods=['POST'])
def process_form():
    print(f"Form form request=={request.form}")
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    session["email"] = request.form["email"]
    User.create_user(request.form)
    return redirect("/display") 

@app.route('/display')
def display(): 
    users=User.get_all() 
    print(users)
    return render_template("read.html",users=users)
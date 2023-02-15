from flask import Flask
app=Flask(__name__)
app.secret_key="login_registration"
DATABASE = "login_register_db"
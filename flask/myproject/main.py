from flask import Flask, render_template, redirect, request
import json


app = Flask(__name__)
app.config["SECRET_KEY"]= "palavra-secreta"
@app.route('/')
def home():
    return render_template('login.html')

if __name__ in "__main__":
    app.run(debug=True)


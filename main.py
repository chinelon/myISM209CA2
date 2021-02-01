from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # create a flask app named app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bookexampledbpassword@localhost:5433/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route("/")
def home():
    return '''My name is Chinelo Nwobbi. This is my CA2 work.
    My GitHub URL is https://github.com/chinelon'''
    # In the return statement above, Use your own name and GitHub URL


@app.route("/home/")
def home2():
    return render_template('home.html', title="Home")


@app.route("/register/")
def register():
    return render_template('register.html', title="Register")


@app.route("/registeredusers")
def registered():
    return render_template('registeredusers.html', title="Registered", information="See registered users here")


if __name__ == "__main__":
    app.run(port=5005)

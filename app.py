from flask import Flask, render_template
import math as m


app = Flask(__name__)

@app.route("/")
def root():
    return render_template("base.html.j2")


@app.route("/abc")
def abc():
    pi = math.pi
    return render_template("abc.html.j2")
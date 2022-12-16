from denter import app
from flask import render_template #request, session, flash, redirect, url_for, jsonify



#pocetna stranica
@app.route("/", methods=["GET"])
def index():
    #ako je korisnik prijavljen 
    return render_template("prijava.html")
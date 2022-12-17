from denter import app, db
from flask import render_template, redirect, url_for, flash, session #request, flash, jsonify
from denter.obrasci import RegistracijaObrazac, PrijavaObrazac
from denter.modeli import Korisnik
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash

#dekorator za prijavu
def potrebna_prijava(f):
    @wraps(f)
    def dekorator(*args, **kwargs):
        if session.get("korisnik_id") is None:
            return redirect("/prijava")
        return f(*args, **kwargs)
    return dekorator

@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("prijava"))

@app.route("/home", methods=["GET"])
@potrebna_prijava
def home():
    return render_template("home.html")

@app.route("/prijava", methods=["GET", "POST"])
def prijava():
    obrazac = PrijavaObrazac()
    
    if obrazac.validate_on_submit():
        korisnik = Korisnik.query.filter_by(email=obrazac.email.data).first()

        #ako postoji korisnik i tocna je lozinka
        if korisnik and check_password_hash(korisnik.lozinka, obrazac.lozinka.data):
            #spremi korisnikov jedinstveni id u session
            session['korisnik_id'] = korisnik.id
            flash(f'uspjesan login za {obrazac.email.data}', 'dobro')
            return redirect(url_for('home'))

        flash("nevažeći email ili lozinka", 'lose')

    return render_template("prijava.html", naslov='prijava', obrazac=obrazac)

@app.route("/registracija", methods=["GET", "POST"])
def registracija():
    obrazac = RegistracijaObrazac()

    if obrazac.validate_on_submit():
        #generacija hasha
        lozinka_hash = generate_password_hash(obrazac.lozinka.data)
        korisnik = Korisnik(ime=obrazac.ime.data, email=obrazac.email.data, lozinka=lozinka_hash)
        db.session.add(korisnik)
        db.session.commit()

        #spremanje logina u kolacic
        session["korisnik_id"] = korisnik.id
        flash('Bok ' + obrazac.ime.data + ', uspiješno ste registrirani', 'dobro')

        return redirect(url_for('home'))

    return render_template('registracija.html', naslov='registracija', obrazac=obrazac)

@app.route("/odjava")
def odjava():
    #izbrisi session
    session.clear()
    return redirect("/")
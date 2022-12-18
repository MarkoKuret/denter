from denter import app, db
from flask import render_template, redirect, url_for, flash, session, request # flash, jsonify
from denter.obrasci import RegistracijaObrazacOsoblje, PrijavaObrazac, RegistracijaObrazacKlijenti
from denter.modeli import Korisnik
#from denter.add_event import events
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
    return redirect(url_for("pocetna"))

@app.route("/home", methods=["GET"])
@potrebna_prijava
def home():
    return render_template("pocetna.html")

@app.route("/prijava", methods=["GET", "POST"])
def prijava():
    obrazac = PrijavaObrazac()
    
    if obrazac.validate_on_submit():
        korisnik = Korisnik.query.filter_by(email=obrazac.email.data).first()

        #ako postoji korisnik i tocna je lozinka
        if korisnik and check_password_hash(korisnik.lozinka, obrazac.lozinka.data):
            #spremi korisnikov jedinstveni id u session
            session['korisnik_id'] = korisnik.id
            flash(f'uspješan login za {obrazac.email.data}', 'dobro')
            return redirect(url_for('home'))

        flash("nevažeći email ili lozinka", 'lose')

    return render_template("prijava.html", naslov='prijava', obrazac=obrazac)

@app.route("/registracija_klijenti", methods=["GET", "POST"])
def registracija_klijenti():
    obrazac = RegistracijaObrazacKlijenti()

    if obrazac.validate_on_submit():
        #generacija hasha
        lozinka_hash = generate_password_hash(obrazac.lozinka.data)
        korisnik = Korisnik(ime=obrazac.ime.data, email=obrazac.email.data, lozinka=lozinka_hash)
        db.session.add(korisnik)
        db.session.commit()

        #spremanje logina u kolacic
        session["korisnik_id"] = korisnik.id
        flash('Bok ' + obrazac.ime.data + ', uspješno ste registrirani', 'dobro')

        return redirect(url_for('home'))

    return render_template('registracija_klijenti.html', naslov='registracija', obrazac=obrazac)

@app.route("/registracija_osoblje", methods=["GET", "POST"])
def registracija_osoblje():
    obrazac = RegistracijaObrazacOsoblje()

    if obrazac.validate_on_submit():
        #generacija hasha
        lozinka_hash = generate_password_hash(obrazac.lozinka.data)
        korisnik = Korisnik(ime=obrazac.ime.data, email=obrazac.email.data, lozinka=lozinka_hash)
        db.session.add(korisnik)
        db.session.commit()

        #spremanje logina u kolacic
        session["korisnik_id"] = korisnik.id
        flash('Bok ' + obrazac.ime.data + ', uspješno ste registrirani', 'dobro')

        return redirect(url_for('home'))

    return render_template('registracija_osoblje.html', naslov='registracija', obrazac=obrazac)

@app.route("/odjava")
def odjava():
    #izbrisi session
    session.clear()
    return redirect("/")

@app.route("/odabir")
def odabir():
    #odabir vrste korisnika
    return render_template('odabir.html')

@app.route("/pocetna")
def pocetna():
    #otvaranje pocetne stranice
    return render_template('pocetna.html')

@app.route("/calendar")
def calendar():
    return render_template('calendar.html') 


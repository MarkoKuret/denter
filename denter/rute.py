from denter import app, db
from flask import render_template, redirect, url_for, flash, session #request, flash, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from denter.obrasci import OsobljeRegistracijaObrazac, PrijavaObrazac, PacijentRegistracijaObrazac, TerminObrazac
from denter.modeli import Uloga, Pacijent, Osoblje, Korisnik, Termin
from denter.calendar_events import events
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from datetime import datetime

def potrebna_uloga(uloga):
    def dekorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            if not current_user.ima_ulogu(uloga):
                return redirect("/prijava")
            else:
                return func(*args, **kwargs)
        return wrapped_function
    return dekorator

@app.route("/", methods=["GET"])
@login_required
def index():
    return redirect(url_for("pocetna"))

@app.route("/prijava", methods=["GET", "POST"])
def prijava():
    obrazac = PrijavaObrazac()

    if current_user.is_authenticated:
        return redirect(url_for('pocetna'))
    
    if obrazac.validate_on_submit():
        korisnik = Korisnik.query.filter_by(email=obrazac.email.data).first()

        #ako postoji Pacijent i tocna je lozinka
        if korisnik and check_password_hash(korisnik.lozinka, obrazac.lozinka.data):
            #spremi Pacijentov jedinstveni id u session
            login_user(korisnik, remember=obrazac.zapamti.data)
            return redirect(url_for('pocetna'))

        flash("Nevažeći email ili lozinka", 'lose')

    return render_template("prijava.html", naslov='prijava', obrazac=obrazac)

@app.route("/registracija_klijenti", methods=["GET", "POST"])
def registracija_klijenti():
    obrazac = PacijentRegistracijaObrazac()

    if current_user.is_authenticated:
            return redirect(url_for('pocetna'))

    if obrazac.validate_on_submit():
        lozinka_hash = generate_password_hash(obrazac.lozinka.data)
        pacijent = Pacijent(ime=obrazac.ime.data, prezime=obrazac.prezime.data, OIB=obrazac.oib.data, email=obrazac.email.data, lozinka=lozinka_hash)
        uloga = Uloga.query.filter_by(tipUloge="pacijent").first()
        uloga.korisnici.append(pacijent)
        db.session.add(pacijent)
        db.session.commit()

        login_user(pacijent)

        flash('Bok ' + obrazac.ime.data + ', uspješno ste registrirani', 'dobro')

        return redirect(url_for('pocetna'))

    return render_template('registracija.html', naslov='Registracija pacijenta', obrazac=obrazac)

@app.route("/registracija_osoblje", methods=["GET", "POST"])
def registracija_osoblje():
    obrazac = OsobljeRegistracijaObrazac()

    if current_user.is_authenticated:
        return redirect(url_for('pocetna'))

    if obrazac.validate_on_submit():
        lozinka_hash = generate_password_hash(obrazac.lozinka.data)
        osoblje = Osoblje(ime=obrazac.ime.data, prezime=obrazac.prezime.data, OIB=obrazac.oib.data, email=obrazac.email.data, lozinka=lozinka_hash)
        uloga = Uloga.query.filter_by(tipUloge="osoblje").first()
        uloga.korisnici.append(osoblje)
        db.session.add(osoblje)
        db.session.commit()

        login_user(osoblje)
        
        flash('Bok ' + obrazac.ime.data + ', uspješno ste registrirani', 'dobro')

        return redirect(url_for('pocetna'))

    return render_template('registracija.html', naslov='Registracija osoblja', obrazac=obrazac)

@app.route("/odjava")
def odjava():
    #izbrisi session
    logout_user()
    return redirect("/")

@login_required
@app.route("/odabir")
def odabir():
    #odabir vrste Pacijenta
    return render_template('odabir.html')

@app.route("/pocetna")
def pocetna():
    #otvaranje pocetne stranice
    return render_template('pocetna.html')

@app.route("/kalendar", methods=["GET", "POST"])
def kalendar():
    obrazac = TerminObrazac()

    if obrazac.validate_on_submit():
        title = obrazac.naziv
        date = obrazac.datum
        time = obrazac.pocetak
        end = obrazac.kraj
        events.append({
            'title': title.data,
            'start': date.data + " " + time.data,
            'end': end.data
        })
        print(events)

        datumVrijeme = obrazac.datum.data + obrazac.pocetak.data

        start = datetime.strptime(obrazac.datum.data, "%Y-%m-%d")
        kraj = start
        termin = Termin(naziv=obrazac.naziv.data, datum_start=start, datum_kraj=kraj)
        db.session.add(termin)
        db.session.commit()


        return redirect(url_for('kalendar'))

    return render_template('kalendar.html', events=events, naslov='dodavnaje termina', obrazac=obrazac)
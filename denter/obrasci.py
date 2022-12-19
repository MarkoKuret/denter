from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, BooleanField #TextAreaField
#from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from denter.modeli import Korisnik
from flask import session

#obrazac za prijavu
class PrijavaObrazac(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    lozinka = PasswordField('Lozinka', validators=[DataRequired()])
    zapamti = BooleanField('Zapamti me')
    submit = SubmitField('Prijavi se')

#obrazac za registraciju_klijenta
class RegistracijaObrazacKlijenti(FlaskForm):
    ime = StringField('Korisničko ime', validators=[DataRequired(), Length(min=3, max=20)])
    prezime = StringField('Korisničko prezime', validators=[DataRequired(), Length(min=3, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    lozinka = PasswordField('Lozinka', validators=[DataRequired()])
    potvrda = PasswordField('Potvrda lozinke', validators=[DataRequired(), EqualTo('lozinka')])
    submit = SubmitField('Registriraj se')
    oib = StringField('OIB', validators=[DataRequired(), Length(min =11, max=11)])

    #obrazac za registraciju_osoblja
class RegistracijaObrazacOsoblje(FlaskForm):
    ime = StringField('Korisničko ime', validators=[DataRequired(), Length(min=3, max=20)])
    prezime = StringField('Korisničko prezime', validators=[DataRequired(), Length(min=3, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    lozinka = PasswordField('Lozinka', validators=[DataRequired()])
    potvrda = PasswordField('Potvrda lozinke', validators=[DataRequired(), EqualTo('lozinka')])
    submit = SubmitField('Registriraj se')
    oib = StringField('OIB', validators=[DataRequired(), Length(min =11, max=11)])

#obrazac sa dodavanje termina
class TerminObrazac(FlaskForm):
    ime = StringField('Naziv termina', )
    datum = StringField('Datum termina', validators=[DataRequired()])
    pocetak = StringField('vrijeme termina', validators=[DataRequired()])
    kraj = StringField('Kraj termina') #trenutno se ne koristi
    submit = SubmitField('Dodaj')


    #provjera jedinstvenosti korisnickog imena
    def validate_ime(self, ime):
        korisnik = Korisnik.query.filter_by(ime=ime.data).first()
        if korisnik:
            raise ValidationError('Zauzeto')

    #provjera jedinstvenosti email-a
    def validate_email(self, email):
        korisnik = Korisnik.query.filter_by(email=email.data).first()
        if korisnik:
            raise ValidationError('Već registriran')
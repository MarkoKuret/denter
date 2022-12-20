from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, BooleanField #TextAreaField
#from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from denter.modeli import Korisnik
from flask import session

#obrazac za prijavu
class PrijavaObrazac(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    lozinka = PasswordField('Lozinka', validators=[DataRequired(), Length(min=3, max=30)])
    zapamti = BooleanField('Zapamti me')
    submit = SubmitField('Prijavi se')

def oib_provjera(form, field):
    korisnik = Korisnik.query.filter_by(OIB=field.data).first()
    if korisnik:
        raise ValidationError('Zauzeto')

def validate_email(form, field):
    korisnik = Korisnik.query.filter_by(email=field.data).first()
    if korisnik:
        raise ValidationError('Zauzeto')

#obrazac za registraciju_klijenta
class PacijentRegistracijaObrazac(FlaskForm):
    ime = StringField('Korisničko ime', validators=[DataRequired(), Length(min=3, max=20)])
    prezime = StringField('Korisničko prezime', validators=[DataRequired(), Length(min=3, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    lozinka = PasswordField('Lozinka', validators=[DataRequired(), Length(min=3, max=30)])
    potvrda = PasswordField('Potvrda lozinke', validators=[DataRequired(), EqualTo('lozinka')])
    submit = SubmitField('Registriraj se')
    oib = StringField('OIB', validators=[DataRequired(), Length(min =11, max=11), oib_provjera])

class OsobljeRegistracijaObrazac(FlaskForm):
    ime = StringField('Korisničko ime', validators=[DataRequired(), Length(min=3, max=20)])
    prezime = StringField('Korisničko prezime', validators=[DataRequired(), Length(min=3, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    lozinka = PasswordField('Lozinka', validators=[DataRequired(), Length(min=3, max=30)])
    potvrda = PasswordField('Potvrda lozinke', validators=[DataRequired(), EqualTo('lozinka')])
    submit = SubmitField('Registriraj se')
    oib = StringField('OIB', validators=[DataRequired(), Length(min =11, max=11), oib_provjera])

#obrazac sa dodavanje termina
class TerminObrazac(FlaskForm):
    naziv = StringField('Naziv termina', )
    datum = StringField('Datum termina', validators=[DataRequired()])
    pocetak = StringField('vrijeme termina', validators=[DataRequired()])
    kraj = StringField('Kraj termina') #trenutno se ne koristi
    submit = SubmitField('Dodaj')

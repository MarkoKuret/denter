from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, BooleanField #TextAreaField
#from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from denter.modeli import Korisnik
#from flask import session

#obrazac za prijavu
class PrijavaObrazac(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    lozinka = PasswordField('Lozinka', validators=[DataRequired()])
    zapamti = BooleanField('Zapamti me')
    submit = SubmitField('Prijavi se')

#obrazac za registraciju
class RegistracijaObrazac(FlaskForm):
    ime = StringField('Korisničko ime', validators=[DataRequired(), Length(min=3, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    lozinka = PasswordField('Lozinka', validators=[DataRequired()])
    potvrda = PasswordField('Potvrda lozinke', validators=[DataRequired(), EqualTo('lozinka')])
    submit = SubmitField('Registriraj se')

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
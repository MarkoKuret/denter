from denter import db, login_manager
from flask_login import UserMixin
from flask_security import RoleMixin

@login_manager.user_loader
def load_user(user_id):
    return Korisnik.query.get(user_id)

uloge_korisnik = db.Table('uloge_korisnik',
    db.Column('korisnik_id', db.Integer(), db.ForeignKey('korisnik.id')),
    db.Column('uloga_tipUloge', db.Integer(), db.ForeignKey('uloga.tipUloge')))

class Uloga(db.Model, RoleMixin):
    __tablename__ = 'uloga'
    tipUloge = db.Column(db.String(8), unique=True, primary_key=True)

class Korisnik(db.Model, UserMixin):
    __tablename__ = 'korisnik'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    OIB = db.Column(db.Integer, unique=True, nullable=False)
    ime = db.Column(db.String(20), nullable=False)
    prezime = db.Column(db.String(20), nullable=False)
    email =  db.Column(db.String(120), unique=True, nullable=False)
    lozinka = db.Column(db.Text, nullable=False)
    opis = db.Column(db.Text)
    avatar = db.Column(db.String(20), nullable=False, default='avatar.svg')
    uloga = db.relationship('Uloga', secondary=uloge_korisnik,
                        backref=db.backref('korisnici', lazy='dynamic'))
     #eobv = db.Column(db.Boolean, default=True, nullable=False)

    def ima_ulogu(self, uloga):
        moja_uloga = Uloga.query.filter_by(tipUloge=uloga).first()
        if moja_uloga in self.uloga:
            return True
        else:
            return False

class Pacijent (Korisnik):
    __tablename__ = 'pacijent'
    __mapper_args__ = {'polymorphic_identity': 'pacijent'}
    zubni_karton = db.Column(db.String(20), default='karton.pdf')

class Osoblje (Korisnik):  
    __tablename__ = 'osoblje'
    __mapper_args__ = {'polymorphic_identity': 'osoblje'}
    id_ordinacije = db.Column(db.Integer, db.ForeignKey('ordinacija.id'), nullable=True)

class Ordinacija(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voditelj = db.Column(db.String(20), nullable=False)
    lokacija = db.Column(db.String(120), nullable=False)
    kontakt = db.Column(db.String(20), unique=True)
    opis = db.Column(db.Text)

class Usluga (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cijena = db.Column(db.Integer, nullable=False)
    opis = db.Column(db.Text)

#Osoblje_Termin = db.Table("Osoblje_Termin", 
#    db.Column("osoblje_id", db.Integer(), db.ForeignKey('osoblje.id')),
#    db.Column("termin_id", db.Integer(), db.ForeignKey('termin.id')))

class Termin (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pacijent = db.Column(db.Integer, db.ForeignKey('pacijent.id'), nullable=False)
    #usluga = db.Column(db.Integer, db.ForeignKey('usluga.id'), nullable=False)
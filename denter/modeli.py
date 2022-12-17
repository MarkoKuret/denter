from denter import db

class Korisnik(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(20), unique=True, nullable=False)
    email =  db.Column(db.String(120), unique=True, nullable=False)
    lozinka = db.Column(db.Text, nullable=False)
    #lozinka = db.Column(db.String(60), nullable=False)
    avatar = db.Column(db.String(20), nullable=False, default='avatar.svg')
    #eobv = db.Column(db.Boolean, default=True, nullable=False)

class Ordinacija(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voditelj = db.Column(db.String(20), nullable=False)
    lokacija = db.Column(db.String(120), nullable=False)
    kontakt = db.Column(db.String(20), unique=True)
    opis = db.Column(db.Text)

class Osoblje (db.Model):
    OIB = db.Column(db.Integer, primary_key=True)
    id_ordinacije = db.Column(db.Integer, db.ForeignKey('Ordinacija.id'), nullable=False)
    ime = db.Column(db.String(20), nullable=False)
    prezime = db.Column(db.String(20), nullable=False)
    email =  db.Column(db.String(120), unique=True, nullable=False)
    lozinka = db.Column(db.Text, nullable=False)
    opis = db.Column(db.Text)

class Pacijent (db.Model):
    OIB = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(20), nullable=False)
    prezime = db.Column(db.String(20), nullable=False)
    email =  db.Column(db.String(120), unique=True, nullable=False)
    lozinka = db.Column(db.Text, nullable=False)
    opis = db.Column(db.Text)
    zubni_karton = db.Column(db.Text)

class Termin (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pacijent = db.Column(db.Integer, db.ForeignKey('Pacijent.OIB'), nullable=False)
    usluga = db.Column(db.Integer, db.ForeignKey('Usluga.id'), nullable=False)
    datum = db.Column(db.DateTime, nullable=False)

Osoblje_Termin = db.Table("Osoblje_Termin", 
    db.Column("Osoblje_OIB", db.Integer, db.ForeignKey('Osoblje.OIB')),
    db.Column("Termin_id", db.Integer, db.ForeignKey('Termin.id'))
)

class Usluga (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cijena = db.Column(db.Integer,nullable=False)
    opis = db.Column(db.Text)








    def __repr__(self):
        return f"Korisnik('{self.ime}', '{self.email}')"
from denter import db

class Korisnik(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(20), unique=True, nullable=False)
    email =  db.Column(db.String(120), unique=True, nullable=False)
    lozinka = db.Column(db.Text, nullable=False)
    #lozinka = db.Column(db.String(60), nullable=False)
    avatar = db.Column(db.String(20), nullable=False, default='avatar.svg')
    #eobv = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return f"Korisnik('{self.ime}', '{self.email}')"
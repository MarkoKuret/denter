from denter import db
from denter.modeli import Uloga

db.drop_all()
db.create_all()

uloga_pacijent = Uloga(tipUloge="pacijent")
uloga_osoblje = Uloga(tipUloge="osoblje")

db.session.add(uloga_osoblje)
db.session.add(uloga_pacijent)

db.session.commit()
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Produkt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(100), nullable=False)
    cena = db.Column(db.Float, nullable=False)
    dostepny = db.Column(db.Boolean, default=True)

    def cena_brutto(self):
        return round(self.cena * 1.23, 2)

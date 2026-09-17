from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sklep.db"
db = SQLAlchemy(app)


# Zadanie 1
@app.route("/")
def index():
    return render_template("index.html", imie="ksawier")

# zadanie 1 - 07


class produkt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(100), nullable=False)
    cena = db.Column(db.Float, nullable=False)
    dostepny = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<Produkt {self.nazwa}>"

@app.route("/")
def lista():
    produkty = Produkt.query.order_by(Produkt.nazwa).all()
    return render_template("lista.html", produkty=produkty)

@app.route("/produkt/<int:id>")
def szczegoly(id):
    p = Produkt.query.get_or_404(id)
    return render_template("produkt.html", p=p)

@app.route("/dodaj", methods=["GET", "POST"])
def dodaj():
    if request.method == "POST":
        p = Produkt(nazwa=request.form["nazwa"],
                    cena=float(request.form["cena"]))
        db.session.add(p)
        db.session.commit()
        return redirect(url_for("lista"))
    return render_template("dodaj.html")

@app.route("/usun/<int:id>", methods=["POST"])
def usun(id):
    p = Produkt.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()
    return redirect(url_for("lista"))


# zadanie 3

# zadanie 4

# zadanie 6
@app.route("/szukaj")
def szukaj():
    q = request.args.get("q", "")
    wyniki = [p for p in PRODUKTY if q.lower() in p["nazwa"].lower()]
    return render_template("szukaj.html", q=q, wyniki=wyniki)

# zadanie 7

@app.route("/dodaj", methods=["GET", "POST"])
def dodaj():
    if request.method == "POST":
        nowy = {
            "id": len(PRODUKTY) + 1,
            "nazwa": request.form["nazwa"],
            "cena": float(request.form["cena"]),
            "dostepny": True,
        }
        PRODUKTY.append(nowy)
        return redirect(url_for("produkty"))
    return render_template("dodaj.html")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
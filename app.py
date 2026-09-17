from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Zadanie 1
@app.route("/")
def index():
    return render_template("index.html", imie="ksawier")

# Zadanie 2

PRODUKTY = [
 {"id": 1, "nazwa": "Laptop", "cena": 2999, "dostepny": True},
 {"id": 2, "nazwa": "Mysz", "cena": 49, "dostepny": False},
 {"id": 3, "nazwa": "Klawiatura", "cena": 199, "dostepny": True},
]
@app.route("/produkty")
def produkty():
 return render_template("produkty.html", produkty=PRODUKTY)
@app.route("/ceny")
def ceny():
 return render_template("ceny.html", ceny={"Laptop": 2999, "Mysz": 49})
@app.route("/lista")
def lista():
 return render_template("lista.html", produkty=["Laptop", "Mysz", "Klawiatura"])

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



if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, abort, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "strona główna"
# zadanie 1
@app.route("/czesc/<imie>")
def czesc(imie):
    return "czesc" + imie

@app.route("/czesc1/<imie>/<wiek>")
def czesc1(imie, wiek):
    return f"czesc  {imie}, masz  {wiek}  lat"
# zadanie 2
@app.route("/dodaj/<int:a>/<int:b>")
def dodaj(a, b):
    return f"wynik to {a + b} "

@app.route("/odejmij/<int:a>/<int:b>")
def odejmij(a, b):
    return f"wynik to {a - b} "

@app.route("/pomnoz/<int:a>/<int:b>")
def pomnoz(a, b):
    return f"wynik to {a * b} "

@app.route("/podziel/<int:a>/<int:b>")
def podziel(a, b):
    return f"wynik to {a / b} "

@app.route("/potenga/<int:a>/<int:b>")
def potenga(a, b):
    return f"wynik to {a ** b} "

# zadanie 3

@app.route("/tabliczka/<int:n>")
def tabliczka(n):
    if not (1 <= n <= 20):
        abort(400)
    wynik = []
    for i in range(1,11):
        wynik.append(f"{n} * {i} = {n * i}")

    return "\n".join(wynik), 200, {'Content-Type': 'text/plain; charset=utf-8'}
# zadanie 4
@app.route("/produkty")
def produkty():
    kat = request.args.get("kategoria")
    cena = request.args.get("cena")
    nazwa = request.args.get("nazwa")

    return f"kategoria: {kat}, sortowanie: {cena}, {nazwa} "

# zadanie 5

@app.route("/element/<int:id>")
def element(id):
    slownik = {1: "produkty", 2: "ogloszenia", 3: "sale", 4: "posty"}
    return slownik[id]

# zadanie 6

@app.route("/start")
def start():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)


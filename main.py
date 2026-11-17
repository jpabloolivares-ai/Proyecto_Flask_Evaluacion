from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "clave-local-evaluacion"

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        try:
            notas = [float(request.form[f"nota{i}"]) for i in range(1, 4)]
            asistencia = float(request.form["asistencia"])
            if any(n < 10 or n > 70 for n in notas):
                flash("Las notas deben estar entre 10 y 70.")
                return render_template("ejercicio1.html")
            if asistencia < 0 or asistencia > 100:
                flash("La asistencia debe estar entre 0 y 100.")
                return render_template("ejercicio1.html")
            promedio = sum(notas) / 3
            estado = "APROBADO" if promedio >= 40 and asistencia >= 75 else "REPROBADO"
            return render_template("resultado1.html", promedio=round(promedio, 2),
                                   asistencia=asistencia, estado=estado)
        except (ValueError, KeyError):
            flash("Ingresa valores numéricos válidos.")
    return render_template("ejercicio1.html")

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":
        nombres = [request.form.get(f"nombre{i}", "").strip() for i in range(1, 4)]
        if any(not n for n in nombres):
            flash("Debes ingresar los tres nombres.")
            return render_template("ejercicio2.html")
        cantidad = max(len(n) for n in nombres)
        mayores = [n for n in nombres if len(n) == cantidad]
        return render_template("resultado2.html", nombres=nombres,
                               mayores=mayores, cantidad=cantidad)
    return render_template("ejercicio2.html")

if __name__ == "__main__":
    app.run(debug=True)

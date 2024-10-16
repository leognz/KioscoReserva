from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar la reserva
@app.route('/reservar', methods=['POST'])
def reservar():
    nombre = request.form['nombre']
    rol = request.form['rol']
    fecha = request.form['fecha']
    hora_inicio = request.form['hora_inicio']
    hora_fin = request.form['hora_fin']
    espacio = request.form['espacio']

    # Guardar los datos en el archivo CSV
    with open('reservas.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre, rol, fecha, hora_inicio, hora_fin, espacio])

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

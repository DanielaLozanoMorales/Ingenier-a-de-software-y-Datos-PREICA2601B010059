import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Esto soluciona problemas de rutas en Windows
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = "autos_colombia_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'autos_colombia.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Registro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(10), nullable=False)
    tipo = db.Column(db.String(20))
    celda = db.Column(db.String(10))
    fecha_ingreso = db.Column(db.DateTime, default=datetime.now)
    fecha_salida = db.Column(db.DateTime, nullable=True)

@app.route('/')
def index():
    # Consultamos todos para ver si se guardaron
    vehiculos = Registro.query.all()
    print(f"DEBUG: Vehículos encontrados en la DB: {len(vehiculos)}") # Esto saldrá en tu terminal
    return render_template('index.html', vehiculos=vehiculos)

@app.route('/ingreso', methods=['POST'])
def registrar_ingreso():
    placa = request.form.get('placa')
    tipo = request.form.get('tipo')
    celda = request.form.get('celda')
    
    print(f"DEBUG: Intentando registrar -> Placa: {placa}, Celda: {celda}") # Ver si llegan los datos
    
    if placa:
        nuevo = Registro(placa=placa.upper(), tipo=tipo, celda=celda)
        db.session.add(nuevo)
        db.session.commit()
        print("DEBUG: ¡Guardado exitosamente en la base de datos!")
    
    return redirect(url_for('index'))

@app.route('/salida/<int:id>')
def registrar_salida(id):
    vehiculo = Registro.query.get(id)
    if vehiculo:
        vehiculo.fecha_salida = datetime.now()
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
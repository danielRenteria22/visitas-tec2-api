from flask import Flask, request, jsonify,Response
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

app.secret_key = 'ECOSYSMART_RANDOM_KEY_16550566'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:3838380814@localhost/visitas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# Models import
from Models.AdminUser import AdminUser
from Models.Alumno import Alumno
from Models.Chofer import Chofer
from Models.Grupo import Grupo
from Models.Kardex import Kardex
from Models.Maestro import Maestro
from Models.Materia import Materia
from Models.MateriaHasHorario import MateriaHasHorario
from Models.Solicitud import Solicitud
from Models.Transporte import Transporte

#Controllers import

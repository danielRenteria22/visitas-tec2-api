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
from Models.Horario import Horario
from Models.Maestro import Maestro
from Models.Materia import Materia
from Models.MateriaHasHorario import MateriaHasHorario
from Models.Solicitud import Solicitud
from Models.Transporte import Transporte

#Controllers import
from Controllers.MaestroController import MaestroController
from Controllers.SolicitudesController import SolicitudesController

#Rutas inicial
@app.route('/')
def index():
    return 'Puedes encontrar la documentacion aqui: '


#Rutas maestros
@app.route('/maestro/all', methods=['GET'])
def allMaestros(id=None):
    return MaestroController.all()

@app.route('/maestro/<int:id>', methods=['GET'])
def maestroIndex(id=None):
    return MaestroController.index(id)


#Rutas Solicitudes
@app.route('/solicitud/create', methods=['POST'])
def createSolicitud():
    return SolicitudesController.create()

@app.route('/solicitud/index/<int:id>', methods=['GET'])
def indexSolicitud(id=None):
    return SolicitudesController.index(id)

@app.route('/solicitud/all', methods=['GET'])
def allSolicitud(id=None):
    return SolicitudesController.all()

@app.route('/solicitud/update/<int:id>', methods=['POST'])
def updateSolicitud(id=None):
    return SolicitudesController.update(id)

@app.route('/solicitud/delete/<int:id>', methods=['DELETE'])
def deleteSolicitud(id=None):
    return SolicitudesController.delete(id)

@app.route('/solicitud/aprove/<int:id>', methods=['POST'])
def aproveSolicitud(id=None):
    return SolicitudesController.aprove(id)

@app.route('/solicitud/unaprove/<int:id>', methods=['POST'])
def unaproveSolicitud(id=None):
    return SolicitudesController.unaprove(id)

@app.route('/solicitud/assign/transport/<int:id>', methods=['POST'])
def assignTransportSolicitud(id=None):
    return SolicitudesController.assignTransport(id)


#Rutas choferes
@app.route('/choferes/all', methods=['GET'])
def allChoferes(id=None):
    return Response("Not yet implemented",500)

@app.route('/choferes/<int:id>', methods=['GET'])
def indexChoferes(id=None):
    return Response("Not yet implemented",500)

@app.route('/choferes/disponibles', methods=['GET'])
def disponiblesChoferes(id=None):
    return Response("Not yet implemented",500)

#Rutas transportes
@app.route('/transportes/all', methods=['GET'])
def alltransportes(id=None):
    return Response("Not yet implemented",500)

@app.route('/transportes/<int:id>', methods=['GET'])
def indexTransportes(id=None):
    return Response("Not yet implemented",500)

@app.route('/transportes/disponibles', methods=['GET'])
def disponiblesTransportes(id=None):
    return Response("Not yet implemented",500)
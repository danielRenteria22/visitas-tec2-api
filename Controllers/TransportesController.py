from app import jsonify,request,db,Response
from datetime import datetime
from Models.Transporte import Transporte

class TransportesController(object):
    @staticmethod
    def all():
        transportes = db.session.query(Transporte).all()
        transportes_json = []
        for transporte in transportes:
            transportes_json.append(transporte.toJson())

        return jsonify(transportes_json)

    @staticmethod
    def index(id,json = True):
        transporte = db.session.query(Transporte).filter_by(id = id).first()
        if(json):
            return jsonify(transporte.toJson())
        else:
            return transporte

    @staticmethod
    def availables():
        return []
        fecha_hora_inicio = request.json.get("fecha_hora_inicio")
        fecha_hora_fin = request.json.get("fecha_hora_fin")
        
        transportes = db.session.query(Transporte).all()
        transportes_disponibles = []
        for transporte in transportes:
            if transporte.isAvailable(fecha_hora_inicio,fecha_hora_fin):
                transportes_disponibles.append(transporte.toJson())
        
        return jsonify(transportes_disponibles)


        
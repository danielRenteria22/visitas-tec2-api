from app import jsonify,request,db,Response
from datetime import datetime
from Models.Chofer import Chofer

class ChoferesController(object):
    @staticmethod
    def all():
        choferes = db.session.query(Chofer).all()
        choferes_json = []
        for chofer in choferes:
            choferes_json.append(chofer.toJson())

        return jsonify(choferes_json)

    @staticmethod
    def index(id,json = True):
        chofer = db.session.query(Chofer).filter_by(id = id).first()
        if(json):
            return jsonify(chofer.toJson())
        else:
            return chofer

    @staticmethod
    def availables():
        return []
        fecha_hora_inicio = request.json.get("fecha_hora_inicio")
        fecha_hora_fin = request.json.get("fecha_hora_fin")
        
        choferes = db.session.query(Chofer).all()
        choferes_disponibles = []
        for chofer in choferes:
            if chofer.isAvailable(fecha_hora_inicio,fecha_hora_fin):
                choferes_disponibles.append(chofer.toJson())
        
        return jsonify(choferes_disponibles)


        
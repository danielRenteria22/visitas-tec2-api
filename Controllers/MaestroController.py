from app import jsonify,request,db,Response
# from models.InvalidUsage import InvalidUsage
from datetime import datetime
from Models.Maestro import Maestro

class MaestroController(object):
    @staticmethod
    def all():
        maestros = db.session.query(Maestro).all()
        maestros_json = []
        for maestro in maestros:
            maestros_json.append(maestro.toJson())

        return jsonify(maestros_json)

    @staticmethod
    def index(id,json = True):
        maestro = db.session.query(Maestro).filter_by(id = id).first()
        maestro.format()
        if(json):
            return jsonify(maestro.toJson())
        else:
            return maestro            
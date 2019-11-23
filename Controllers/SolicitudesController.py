from app import jsonify,request,db,Response
# from models.InvalidUsage import InvalidUsage
from datetime import datetime
from Models.Maestro import Maestro
from Models.Solicitud import Solicitud
from MaestroController import MaestroController

class SolicitudesController(object):
    @staticmethod
    def  create():
        request.get_json(force=True)
        maestro = MaestroController.index(request.json.get("maestro_id"),False)
        if not maestro.hasGrupo(request.json.get("grupo_id")):
            return Response("Este maestro no tiene asignado a este grupo", status=402)

        solicitud = Solicitud(
            maestro_id = request.json.get("maestro_id"),
            grupo_id = request.json.get("grupo_id"),
            descripcion = request.json.get("descripcion"),
            fecha_hora_inicio = request.json.get("fecha_hora_inicio"),
            fecha_hora_fin = request.json.get("fecha_hora_fin")
        )

        db.session.add(solicitud)
        db.session.commit()

        return Response("La solicitud se creo con exito",status = 200)


    @staticmethod
    def index(id,json = True, format = True):
        solicitud = db.session.query(Solicitud).filter_by(id = id).first()
        if not solicitud:
            return Response("Esta solicitud no existe", 403)

        if(format):
            solicitud.format()
        
        if(json):
            return jsonify(solicitud.toJson())
        else:
            return solicitud

    @staticmethod
    def update(id):
        solicitud = db.session.query(Solicitud).filter_by(id = id).first()
        if not solicitud:
            return Response("Esta solicitud no existe", 403)
        if solicitud.aprobada:
            return Response("No se puede aprobar una solicitud que esta aprobada",403)

        solicitud.maestro_id = request.json.get("maestro_id"),
        solicitud.grupo_id = request.json.get("grupo_id"),
        solicitud.descripcion = request.json.get("descripcion"),
        solicitud.fecha_hora_inicio = request.json.get("fecha_hora_inicio"),
        solicitud.fecha_hora_fin = request.json.get("fecha_hora_fin")

        db.session.commit()
        return Response("Se actualizo la informacion",status=200)

    @staticmethod
    def delete(id):
        solicitud = db.session.query(Solicitud).filter_by(id = id).first()
        if not solicitud:
            return Response("Esta solicitud no existe", 403)
        db.session.delete(solicitud)
        db.session.commit()

        return Response("Se elimino la solicitud",200)

        
        
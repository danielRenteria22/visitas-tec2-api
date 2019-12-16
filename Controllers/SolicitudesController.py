from app import jsonify,request,db,Response
# from models.InvalidUsage import InvalidUsage
from datetime import datetime
from Models.Maestro import Maestro
from Models.Solicitud import Solicitud
from MaestroController import MaestroController
from Models.Chofer import Chofer
from Models.Transporte import Transporte

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
            fecha_hora_fin = datetime.now().strftime("%Y/%m/%d, %H:%M:%S"),
            fecha_hora_inicio = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
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
    def all():
        solicitudes = db.session.query(Solicitud).all()
        solicitudes_json = []
        for solicitud in solicitudes:
            solicitudes_json.append(solicitud.toJson())
        
        return jsonify(solicitudes_json)

    @staticmethod
    def update(id):
        solicitud = db.session.query(Solicitud).filter_by(id = id).first()
        if not solicitud:
            return Response("Esta solicitud no existe", 403)
        if solicitud.aprobada:
            return Response("No se puede editar una solicitud que esta aprobada",403)

        solicitud.maestro_id = request.json.get("maestro_id"),
        solicitud.grupo_id = request.json.get("grupo_id"),
        solicitud.descripcion = request.json.get("descripcion")

        db.session.commit()
        return Response("Se actualizo la informacion",status=200)

    @staticmethod
    def delete(id):
        solicitud = db.session.query(Solicitud).filter_by(id = id).first()

        if not solicitud:
            return Response("Esta solicitud no existe", 403)
        if solicitud.aprobada:
            return Response("No se puede eliminar una solicitud que esta aprobada",403)
        db.session.delete(solicitud)
        db.session.commit()

        return Response("Se elimino la solicitud",200)

    @staticmethod
    def aprove(id):
        solicitud = db.session.query(Solicitud).filter_by(id = id).first()

        if not solicitud:
            return Response("Esta solicitud no existe", 403)
        #TODO verificar que el usuario sea un administrador
        solicitud.aprobada = True
        db.session.commit()

        return Response("Se aprobo la solicitud",200)

    @staticmethod
    def unaprove(id):
        solicitud = db.session.query(Solicitud).filter_by(id = id).first()

        if not solicitud:
            return Response("Esta solicitud no existe", 403)
        #TODO verificar que el usuario sea un administrador
        solicitud.aprobada = False
        db.session.commit()

        return Response("Se desaprobo la solicitud",200)

    @staticmethod
    def assignTransport(id):
        solicitud = db.session.query(Solicitud).filter_by(id = id).first()

        if not solicitud:
            return Response("Esta solicitud no existe", 403)
        if not solicitud.fecha_hora_inicio or solicitud.fecha_hora_fin:
            return Response("Para asignar transporte se necesiya fecha y hora de inicio y de fin", 403)

        chofer_id = request.json.get("chofer_id")
        transporte_id = request.json.get("transporte_id")
        chofer = db.session.query(Chofer).filter_by(id = chofer_id).first()
        if not chofer_id:
            return Response("Este chofer no existe",403)

        transporte = db.session.query(Transporte).filter_by(id = transporte_id).first()
        if not transporte:
            return Response("Este transporte no existe",403)

        if not chofer.isAvailable():
            return Response("Este chofer no esta disponible", 403)
        if not transporte.isAvailable():
            return Response("Este transporte no esta disponible", 403)
        
        solicitud.chofer_id = chofer_id
        solicitud.transporte_id = transporte_id

        return Response("Se acualizo la informacion con exito",200)
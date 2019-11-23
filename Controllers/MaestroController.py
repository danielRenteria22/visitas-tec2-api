from app import jsonify,request,db,Response
from datetime import datetime
from Models.Maestro import Maestro
from Models.MateriaHasGrupo import MateriaGrupoHasHoraio

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

    """
    Verifica si los grupos de un maestro tiene visita en un
    una fecha 
    @return regresa un arreglo de grupos con informacion sobre
    si tiene visitas ese dia
    """
    @staticmethod
    def maestroGruposHasVisitas(id_maestro,fecha):
        grupos = db.session.query(MateriaHasGrupo)\
            .filter_by(maestro_id = id_maestro).all()
        
        grupo_has_visitas = []
        for grupo in grupos:
            grupo_has_visitas.append(grupo.grupoHasVisita(fecha))

        return jsonify(grupo_has_visitas)
        
from app import db,jsonify
from sqlalchemy import Column,Integer,DateTime,String,ForeignKey,Boolean,or_
import datetime

class Chofer(db.Model):
    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), unique=False, nullable=False)
    apellidos = Column(String(80), unique=False, nullable=False)

    def toJson(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellidos": self.apellidos
        }

    def isAvailable(self,visita):
        visitas_chofer = db.session.query(Solicitud)\
            .filter_by(chofer_id = self.id)\
            .filter_by(aprobada = True)\
            .filter(or_(Solicitud.fecha_hora_inicio < visita.fecha_hora_fin,
                Solicitud.fecha_hora_fin > visita.fecha_hora_inicio))\
            .first()

        return False if visitas_chofer else True

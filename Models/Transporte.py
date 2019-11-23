from app import db,jsonify
from sqlalchemy import Column,Integer,DateTime,String,ForeignKey,Boolean
import datetime

class Transporte(db.Model):
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(80), unique=False, nullable=False)
    capacidad = Column(Integer, unique=False, nullable=False)

    def toJson(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "capacidad": self.capacidad
        }
    
    def isAvailable(self,visita):
        visitas_transporte = db.session.query(Solicitud)\
            .filter_by(transporte_id = self.id)\
            .filter_by(aprobada = True)\
            .filter(or_(Solicitud.fecha_hora_inicio < visita.fecha_hora_fin,
                Solicitud.fecha_hora_fin > visita.fecha_hora_inicio))\
            .first()

        return False if visitas_chofer else True
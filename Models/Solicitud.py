from app import db,jsonify
from sqlalchemy import Column,Integer,DateTime,String,ForeignKey,Boolean
import datetime

class Solicitud(db.Model):
    id = Column(Integer, primary_key=True)
    created_at =  Column(DateTime, default=datetime.datetime.now)
    maestro_id =  Column(Integer, 
        ForeignKey('maestro.id',ondelete='CASCADE'),
        nullable=False)
    grupo_id =  Column(Integer, 
        ForeignKey('grupo.id',ondelete='CASCADE'),
        nullable=False)
    descripcion = Column(String(80), unique=False, nullable=False)
    fecha_hora_inicio = Column(DateTime,nullable = False)
    fecha_hora_fin = Column(DateTime,nullable = False)
    aprobada = Column(Boolean, unique=False, nullable=False,default=False)
    aprobada_por_id = Column(Integer, 
        ForeignKey('admin_user.id',ondelete='CASCADE'),
        nullable=True) 
    fecha_aprobacion = Column(DateTime,nullable = True)
    transporte_id = Column(Integer, 
        ForeignKey('transporte.id',ondelete='CASCADE'),
        nullable=True)
    chofer_id = Column(Integer, 
        ForeignKey('chofer.id',ondelete='CASCADE'),
        nullable=True) 

    def format(self):
        print("Formating Solicitud")

    def toJson(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "maestro_id": self.maestro_id,
            "grupo_id": self.grupo_id,
            "descripcion": self.descripcion,
            "fecha_hora_inicio": self.fecha_hora_inicio,
            "fecha_hora_fin": self.fecha_hora_fin,
            "aprobada": self.aprobada,
            "aprobada_por_id": self.aprobada_por_id,
            "fecha_aprobacion": self.fecha_aprobacion,
            "transporte_id": self.transporte_id,
            "chofer_id": self.chofer_id
        }

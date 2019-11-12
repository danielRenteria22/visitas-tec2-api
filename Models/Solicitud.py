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
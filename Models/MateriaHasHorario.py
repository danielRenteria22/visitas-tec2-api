from app import db,jsonify
from sqlalchemy import Column,Integer,DateTime,String,ForeignKey,Boolean
import datetime

class MateriaHasHorario(db.Model):
    id = Column(Integer, primary_key=True)
    materia_id =  Column(Integer, 
        ForeignKey('materia.id',ondelete='CASCADE'),
        nullable=False)
    grupo_id =  Column(Integer, 
        ForeignKey('grupo.id',ondelete='CASCADE'),
        nullable=False)
    maestro_id =  Column(Integer, 
        ForeignKey('maestro.id',ondelete='CASCADE'),
        nullable=False)
    hora_inicio = Column(DateTime, unique=False, nullable=True)
    hora_fin  = Column(DateTime, unique=False, nullable=True)
from app import db,jsonify
from sqlalchemy import Column,Integer,DateTime,String,ForeignKey,Boolean
import datetime

class Horario(db.Model):
    id = Column(Integer, primary_key=True)
    alumno_num_control = Column(Integer, 
        ForeignKey('alumno.num_control',ondelete='CASCADE'),
        nullable=False)
    materia_has_horario = Column(Integer, 
        ForeignKey('materia_has_horario.id',ondelete='CASCADE'),
        nullable=False)
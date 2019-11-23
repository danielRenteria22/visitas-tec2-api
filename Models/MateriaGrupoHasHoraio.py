from app import db,jsonify
from sqlalchemy import Column,Integer,DateTime,String,ForeignKey,Boolean
import datetime



class MateriaGrupoHasHoraio(db.Model):
    id = Column(Integer, primary_key=True)
    materia_has_grupo_id = Column(Integer, 
        ForeignKey('materia_has_grupo.id',ondelete='CASCADE'),
        nullable=False)
    hora_inicio = Column(DateTime, unique=False, nullable=False)
    hora_fin  = Column(DateTime, unique=False, nullable=False)
    dia_semana = Column(Integer, unique=False, nullable=False)
from app import db,jsonify
from sqlalchemy import Column,Integer,DateTime,String,ForeignKey,Boolean
from Grupo import Grupo
from Materia import Materia
import datetime

class MateriaHasGrupo(db.Model):
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
    

    def format(self):
        self.grupo = self.getGrupo().toJson()
        self.materia = self.getMateria().toJson()

    def toJson(self):
        return {
            "id": self.id,
            "hora_inicio": self.hora_inicio,
            "hora_fin": self.hora_fin,
            "materia": self.materia if self.materia else self.materia_id,
            "grupo": self.grupo if self.grupo else self.grupo_id
        }

    def getGrupo(self):
        return db.session.query(Grupo).filter_by(id = self.grupo_id).first()

    def getMateria(self):
        return db.session.query(Materia).filter_by(id = self.materia_id).first()
    
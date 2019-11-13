from app import db,jsonify
from sqlalchemy import Column,Integer,DateTime,String,ForeignKey,Boolean
from MateriaHasHorario import MateriaHasHorario
from Grupo import Grupo
import datetime

class Maestro(db.Model):
    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), unique=False, nullable=False)
    apellidos = Column(String(80), unique=False, nullable=False)

    def format(self):
        self.addHorario()
        self.addGrupos()

    def addHorario(self):
        self.horario = self.getHorario()

    def addGrupos(self):
        self.grupos = self.getGrupos()

    def toJson(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "horario": self.horario if self.horario else [],
            "grupos": self.grupos if self.grupos else []
        }

    def getHorario(self):
        horario = db.session.query(MateriaHasHorario).filter_by(maestro_id = self.id).all()
        horario_json = []
        for clase in horario:
            clase.format()
            horario_json.append(clase.toJson())
        
        return horario_json

    def getGrupos(self):
        grupos = db.session.query(MateriaHasHorario.grupo_id).filter_by(maestro_id = self.id).all()
        grupos_id = []
        for grupo in grupos:
            grupos_id.append(grupo[0])

        grupos = db.session.query(Grupo).filter(Grupo.id.in_(grupos_id)).all()
        grupos_json = []
        for grupo in grupos:
            grupos_json.append(grupo.toJson())

        return grupos_json
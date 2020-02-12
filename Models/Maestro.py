from app import db,jsonify
from sqlalchemy import Column,Integer,DateTime,String,ForeignKey,Boolean
from MateriaHasGrupo import MateriaHasGrupo
from MateriaGrupoHasHorario import MateriaGrupoHasHorario
from Grupo import Grupo
import datetime
import copy 

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
            "horario": self.horario if hasattr(self, 'horario') else [],
            "grupos": self.grupos if hasattr(self, 'grupos') else []
        }

    def getHorario(self):
		grupos = db.session.query(MateriaHasGrupo.id).filter_by(maestro_id = self.id).all()
		grupos_id = []
		for grupo in grupos:
			grupos_id.append(grupo[0])


		horario = db.session.query(MateriaGrupoHasHorario).filter(MateriaGrupoHasHorario.materia_has_grupo_id.in_(grupos_id)).all()
		horario_json = []
		for clase in horario:
			clase.format()
			horario_json.append(clase.toJson())

		return horario_json

    def getGrupos(self):
		grupos = db.session.query(MateriaHasGrupo.grupo_id).filter_by(maestro_id = self.id).all()
		grupos_id = []
		for grupo in grupos:
			grupos_id.append(grupo[0])

		grupos = db.session.query(Grupo).filter(Grupo.id.in_(grupos_id)).all()
		grupos_json = []
		for grupo in grupos:
			grupos_json.append(grupo.toJson())

		return grupos_json

    def hasGrupo(self,id_grupo):
		print("id_grupo",id_grupo)
		grupo = db.session.query(MateriaHasGrupo).filter_by(maestro_id = self.id)\
			.filter_by(grupo_id = id_grupo).first()
        
		return True if grupo else False
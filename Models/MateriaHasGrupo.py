from app import db,jsonify,Response
from sqlalchemy import Column,Integer,DateTime,String,ForeignKey,Boolean
from Grupo import Grupo
from Materia import Materia
from MateriaGrupoHasHorario import MateriaGrupoHasHorario
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

    def grupoHasVisita(self,fecha):
        visita = db.session.query(Solicitud)\
            .filter_by(grupo_id = self.grupo_id)\
            .filter_by(aprobada = True)\
            .filter_by(fecha_hora_inicio = fecha)\
            .first()
        
        horario = db.session.query(MateriaGrupoHasHorario)\
            .filter_by(materia_has_grupo_id = self.id)\
            .filter_by(dia_semana = fecha.weekday())

        response = {}
        resonse.grupo = self.getGrupo().toJson()
        if not visita or not horario:
            response.tiene_visita = False
            return Response(response,200)

        response.tiene_visita = True
        response.visita = visita

        if (visita.fecha_hora_inicio >= horario.hora_fin
            and visita.fecha_hora_fin <= horario.hora_inicio):
            response.overlap = False
        else:
            response.overlap = True

        return Response(response,200)
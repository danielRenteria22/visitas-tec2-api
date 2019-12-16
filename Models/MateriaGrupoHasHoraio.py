from app import db,jsonify
from sqlalchemy import Column,Integer,DateTime,String,ForeignKey,Boolean
from Grupo import Grupo
import datetime



class MateriaGrupoHasHoraio(db.Model):
    id = Column(Integer, primary_key=True)
    materia_has_grupo_id = Column(Integer, 
        ForeignKey('materia_has_grupo.id',ondelete='CASCADE'),
        nullable=False)
    hora_inicio = Column(DateTime, unique=False, nullable=False)
    hora_fin  = Column(DateTime, unique=False, nullable=False)
    dia_semana = Column(Integer, unique=False, nullable=False)

    def toJson(self):
        return {
            "id":self.id,
            "hora_inicio": self.hora_inicio.time().strftime('%H:%M'),
            "hora_fin": self.hora_fin.time().strftime('%H:%M'),
            "dia_semana": self.dia_semana,
            "grupo": self.grupo.toJson() if hasattr(self, 'grupo') else None
        }

    def format(self):
        self.addGrupo()
        
    def addGrupo(self):
        self.grupo = self.getGrupo()

    def getGrupo(self):
        from MateriaHasGrupo import MateriaHasGrupo
        materia_has_grupo = db.session.query(MateriaHasGrupo).filter_by(id = self.materia_has_grupo_id).first()
        return db.session.query(Grupo).filter_by(id = materia_has_grupo.grupo_id).first()
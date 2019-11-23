from app import db,jsonify
from sqlalchemy import Column,Integer,DateTime,String,ForeignKey,Boolean
from Grupo import Grupo
from Maestro import Maestro
from AdminUser import AdminUser
from Chofer import Chofer
from Transporte import Transporte
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
        self.addAdminUser()
        self.addChofer()
        self.addMaestro()
        self.addTransporte()
        self.addGrupo()

    def toJson(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "maestro": self.maestro_id if self.maestro else self.maestro_id,
            "grupo": self.grupo if self.grupo else self.grupo_id,
            "descripcion": self.descripcion,
            "fecha_hora_inicio": self.fecha_hora_inicio,
            "fecha_hora_fin": self.fecha_hora_fin,
            "aprobada": self.aprobada,
            "aprobada_por": self.admin_user if self.admin_user else self.aprobada_por_id,
            "fecha_aprobacion": self.fecha_aprobacion,
            "transporte": self.transporte if self.transporte else self.transporte_id,
            "chofer": self.chofer if self.chofer else self.chofer_id
        }

    def getMaestro(self):
        return db.session.query(Maestro).filter_by(id = self.maestro_id).first()

    def getGrupo(self):
        return db.session.query(Grupo).filter_by(id = self.grupo_id).first()

    def getAdminUser(self):
        return db.session.query(AdminUser).filter_by(id = self.aprobada_por_id).first()

    def getChofer(self):
        return db.session.query(Chofer).filter_by(id = self.chofer_id).first()
    
    def getTransporte(self):
        return db.session.query(Transporte).filter_by(id = self.transporte_id).first()

    def addMaestro(self):
        self.maestro = self.getMaestro().toJson()

    def addGrupo(self):
        self.grupo = self.getGrupo().toJson()

    def addAdminUser(self):
        self.admin_user = self.getAdminUser().toJson()

    def addChofer(self):
        self.chofer = self.getChofer().toJson()

    def addTransporte(self):
        self.transporte = self.getTransporte().toJson()
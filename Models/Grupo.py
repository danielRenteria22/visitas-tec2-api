from app import db,jsonify
from sqlalchemy import Column,Integer,DateTime,String,ForeignKey,Boolean
import datetime

class Grupo(db.Model):
    id = Column(Integer, primary_key=True)
    identificador = Column(String(80), unique=False, nullable=False)

    def toJson(self):
        return {
            "id": self.id,
            "identificador": self.identificador
        }
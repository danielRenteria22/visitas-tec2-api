from app import db,jsonify
from sqlalchemy import Column,Integer,DateTime,String,ForeignKey,Boolean
import datetime

class Transporte(db.Model):
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(80), unique=False, nullable=False)
    capacidad = Column(Integer, unique=False, nullable=False)
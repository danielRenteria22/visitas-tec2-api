from app import db,jsonify
from sqlalchemy import Column,Integer,DateTime,String,ForeignKey,Boolean
import datetime

class Chofer(db.Model):
    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), unique=False, nullable=False)
    apellidos = Column(String(80), unique=False, nullable=False)
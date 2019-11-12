from app import db,jsonify
from sqlalchemy import Column,Integer,DateTime,String,ForeignKey,Boolean
import datetime

class AdminUser(db.Model):
    id = Column(Integer, primary_key=True)
    nombre_completo = Column(String(80), unique=False, nullable=False)
    user_name = Column(String(80), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
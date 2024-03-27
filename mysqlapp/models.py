from sqlalchemy import Column, Integer, String,Date,Enum
from .database import Base
# from .enumerations import STATUT,PRIORITE

class STATUT(str, Enum):
        EN_COURS = 'EN_COURS'
        FINI= 'FINI'
        STOPE = 'STOPE'
        EN_ATTENTE = 'EN_ATTENTE'

class PRIORITE(str,Enum):
        HAUTE= 'HAUTE'
        MOYENNE='MOYENNE'
        FAIBLE='FAIBLE'



class Task(Base):
        __tablename__='taches'
        id=Column(Integer,primary_key=True,index=True)
        auteur=Column(String(30),index=True)
        titre=Column(String(30),nullable=False)
        description=Column(String(100),nullable=False)
        statut=Column(Enum('EN_COURS','STOPE','EN_ATTENTE','FINI'),nullable=False,default=STATUT.EN_COURS)
        priorite=Column(Enum('HAUTE','MOYENNE','FAIBLE'),nullable=False,default=PRIORITE.MOYENNE)
        commentaire=Column(String(100),nullable=True)
        date_echeance=Column(Date,nullable=False)
        date_debut=Column(Date,nullable=False)
        date_fin=Column(Date,nullable=True)



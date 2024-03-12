from typing import List, Optional,Tuple
# from enumerations import STATUT,PRIORITE
from datetime import date
from enum import Enum
from pydantic import BaseModel,validator,Field


class STATUT(str,Enum):
    EN_COURS = 'EN_COURS'
    FINI= 'FINI'
    STOPE = 'STOPE'
    EN_ATTENTE = 'EN_ATTENTE'

class PRIORITE(str,Enum):
    HAUTE= 'HAUTE'
    MOYENNE='MOYENNE'
    FAIBLE='FAIBLE'

class TaskBase(BaseModel):
    titre:str=Field(examples=['faire les courses'])
    description:str=Field(examples=['aller au supermarché MOIGNON'])
    statut:STATUT =Field(... ,description="Status de la tache (EN_COURS, EN_ATTENTE, FINI, STOPE)")
    priorite:PRIORITE=Field(..., description="Status de la tache (HAUTE,MOYENNE,HAUTE)")
    commentaire:str=Field(examples=['Cette tache est tres fatiguante la nuit'])


class TaskCreate(TaskBase):
    date_echeance:date=Field(examples=['2024-03-11'])
    date_debut:date =Field(examples=['2024-03-11'])
    date_fin:date =Field(examples=['2024-03-11'])

class Task(TaskCreate):
    id:int
    class Config:
        from_orm = True

class TaskUpdate(BaseModel):
    titre:Optional[str]=None
    description:Optional[str]=None
    statut:Optional[STATUT]=None
    priorite:Optional[PRIORITE]=None
    commentaire:Optional[str]=None
    date_echeance:Optional[date]=None
    date_debut:Optional[date]=None
    date_fin:Optional[date]=None

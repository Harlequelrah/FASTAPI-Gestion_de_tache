from sqlalchemy import Enum
class STATUT(str, Enum):
    EN_COURS = 'EN_COURS'
    FINI= 'FINI'
    STOPE = 'STOPE'
    EN_ATTENTE = 'EN_ATTENTE'

class PRIORITE(str,Enum):
    HAUTE= 'HAUTE'
    MOYENNE='MOYENNE'
    FAIBLE='FAIBLE'

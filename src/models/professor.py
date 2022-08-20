from sqlalchemy import Column, BigInteger, Boolean

from src.models.usuario import UsuarioModel


class ProfessorModel(UsuarioModel):
    __tablename__ = 'professor'

    matricula = Column(BigInteger, nullable=False)
    is_coordenador = Column(Boolean, default=False)
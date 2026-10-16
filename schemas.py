from enum import Enum

from pydantic import BaseModel, Field


class NivelCriticidad(str, Enum):
    BAJA = "baja"
    MEDIA = "media"
    ALTA = "alta"


class ExtraccionTecnica(BaseModel):
    tecnologias: list[str] = Field(
        description="Lista de tecnologías, frameworks, bases de datos o herramientas identificadas en el texto.",
        min_length=1,
    )
    nivel_de_criticidad: NivelCriticidad = Field(
        description="Nivel de criticidad del evento o arquitectura expuesta (baja, media, alta)."
    )
    resumen_tecnico: str = Field(
        description="Resumen conciso y técnico del problema, fallo o arquitectura descrita."
    )
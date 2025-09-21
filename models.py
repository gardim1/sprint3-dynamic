from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Insumo:
    id: int
    nome: str
    validade: date

@dataclass(frozen=True)
class Consumo:
    data: date
    insumo_id: int
    nome: str
    quantidade: int
    validade: date

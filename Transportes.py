from enum import Enum, unique, auto


@unique
class Transportes(Enum):
    Privado = auto()
    Onibus = auto()
    Trem = auto()
    Transferencia = auto()
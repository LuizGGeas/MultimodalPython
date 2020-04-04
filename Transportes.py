from enum import Enum, unique, auto


@unique
class Transportes(Enum):
    Onibus = auto()
    Privado = auto()
    Trem = auto()
    Transferencia = auto()
    No = -1
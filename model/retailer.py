from dataclasses import dataclass


@dataclass
class Retailer:
    codice: str
    nome: str
    tipo: str
    nazione: str

    def __eq__(self, other):
        return self.codice == other.codice

    def __hash__(self):
        return hash(self.codice)

    def __str__(self):
        return self.nome

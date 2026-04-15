from dataclasses import dataclass


@dataclass
class Vendita:
    codiceRetailer: str
    numeroProdotto: int
    data: str
    ricavo: float

    def __eq__(self, other):
        return (self.codiceRetailer == other.codiceRetailer and
                self.numeroProdotto == other.numeroProdotto and
                self.data == other.data and
                self.ricavo == other.ricavo)

    def __hash__(self):
        return hash((self.codiceRetailer, self.numeroProdotto, self.data, self.ricavo))

    def __str__(self):
        return (f"Data: {self.data}; Ricavo: {self.ricavo}; "
                f"Retailer: {self.codiceRetailer}; Product: {self.numeroProdotto}")
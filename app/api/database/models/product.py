"""
Models of product related databases
"""

class Product:
    """ Base class of type Product """
    def __init__(self, ID_Product, Manufacturer, Price) -> None:
        self.ID_Product: int    = ID_Product
        self.Manufacturer: str  = Manufacturer
        self.Price: float       = Price

    def setManufacturer(self, Manufacturer: str) -> None:
        """ Update manufacturer's of this product """
        self.Manufacturer = Manufacturer

    def getManufacturer(self) -> str:
        """ Obtain manufacturer's of this product """
        return self.Manufacturer

    def setPrice(self, Price: float) -> None:
        """ Update the price of this product """
        self.Price = Price

    def getPrice(self) -> float:
        """ Obtain the price of this product """
        return self.Price

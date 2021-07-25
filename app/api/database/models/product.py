"""
Models of product related databases
"""

class Product(object):
    """ Base class of type Product """
    def __init__(self, Product:str, Manufacturer:str, Price:float) -> None:
        self.__product: str       = Product
        self.__manufacturer: str  = Manufacturer
        self.__price: float       = Price

    def __str__(self) -> str:
        return "|%25s|%25s|%12s|" % (str(self.getProduct()),
            str(self.getManufacturer()),
            str("US$ %.2f" % self.getPrice()))

    def setProduct(self, Product: str) -> None:
        """ Update product's description """
        self.__product = Product

    def getProduct(self) -> str:
        """ Obtain this product's description """
        return self.__product

    def setManufacturer(self, Manufacturer: str) -> None:
        """ Update manufacturer's of this product """
        self.__manufacturer = Manufacturer

    def getManufacturer(self) -> str:
        """ Obtain manufacturer's of this product """
        return self.__manufacturer

    def setPrice(self, Price: float) -> None:
        """ Update the price of this product """
        self.__price = Price

    def getPrice(self) -> float:
        """ Obtain the price of this product """
        return self.__price

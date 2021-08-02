"""
Models of product related databases
"""
import datetime

class product:
     def __init__(self, ID_Product: int, Manufacturer: str, Price: float) -> None
         self.ID_Product: int = ID_Product
         self.Manufacturer: str = Manufacturer
         self.Price: float = Price
     
     def setManufacturer(self, Manufacturer: int) -> None:
         self.Manufacturer = Manufacturer

     def getManufacturer(self) -> int:
         return self.Manufacturer

     def setPrice(self, Price: float) -> None:
         self.Price = Price

     def getPrice (self) -> float:
         return self.Price

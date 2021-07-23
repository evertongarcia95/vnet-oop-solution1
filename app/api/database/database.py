"""
Database abstration with all tables of the application
"""

from database.models.people import Person, Customer, Seller
from database.models.product import Product

class database(object):
    """ Base class of database management """
    def __init__(self) -> None:
        # dictionaries to represent the object tables
        self.tablePerson    = {}
        self.tableCustomer  = {}
        self.tableSeller    = {}
        self.tableProduct   = {}
    
    def add(self, objData) -> bool:
        try:
            if (type(objData) == Person):
                self.tablePerson[Person(objData).getIDPerson()] = objData
            elif (type(objData) == Customer):
                self.tablePerson[Customer(objData).getIDCustomer] = objData
            elif (type(objData) == Seller):
                self.tablePerson[Seller(objData).getIDSeller()] = objData
            elif (type(objData) == Product):
                self.tablePerson[Product(objData).getIDProduct()] = objData
        except:
            return False
        finally:
            return True

    def list(self):
        pass
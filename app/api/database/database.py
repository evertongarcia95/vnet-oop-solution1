"""
Database abstration with all tables of the application
"""
from enum import Enum, unique

from .models.people import Customer, Seller
from .models.product import Product

@unique
class tableTypes(Enum):
    """ Enumeration of supported database tables """
    CUSTOMER    = 1
    SELLER      = 2
    PRODUCT     = 3
    SALE        = 4


class Database(object):
    """ Base class of database management """
    def __init__(self) -> None:
        # dictionaries to represent the object tables
        self.tableCustomer  = {}
        self.tableSeller    = {}
        self.tableProduct   = {}


    def __nextID(self, dictTable) -> int:
        """ Private method which return next ID based on current state of
              received table """
        # get current ID of the table
        curID: int = (0 if len(dictTable) == 0 else max(dictTable))
        # return its increment
        return curID + 1


    def add(self, objData) -> bool:
        """ Public method to add a new register into the database """
        try:
            if (type(objData) == Customer):
                self.tableCustomer[self.__nextID(self.tableCustomer)]   = objData
            elif (type(objData) == Seller):
                self.tableSeller[self.__nextID(self.tableSeller)]       = objData
            elif (type(objData) == Product):
                self.tableProduct[self.__nextID(self.tableProduct)]     = objData
            else:
                raise Exception("Error!")

            return True
        except:
            return False


    def getRecord(self, recordType: tableTypes, idToGet: int):
        """ Public method to get register from the database """
        try:
            if recordType == tableTypes.CUSTOMER:
                return self.tableCustomer.get(idToGet)
            elif recordType == tableTypes.SELLER:
                return self.tableSeller.get(idToGet)
            elif recordType == tableTypes.PRODUCT:
                return self.tableProduct.get(idToGet)
            else:
                raise Exception("Error!")
        except:
            return None


    def remove(self, recordType: tableTypes, idToRemove: int) -> bool:
        """ Public method to remove a register from the database """
        try:
            # Depending on record type try to remove it using the infored ID
            #   if it does not exist, or other issue, returns an error
            if recordType == tableTypes.CUSTOMER:
                del self.tableCustomer[idToRemove]
            elif recordType == tableTypes.SELLER:
                del self.tableSeller[idToRemove]
            elif recordType == tableTypes.PRODUCT:
                del self.tableProduct[idToRemove]
            else:
                raise Exception("Error!")

            return True
        except:
            return False


    def update(self, objData, idToUpdate:int) -> bool:
        """ Public method to modify a register of the database """
        try:
            if (type(objData) == Customer):
                self.tableCustomer[idToUpdate]  = objData
            elif (type(objData) == Seller):
                self.tableSeller[idToUpdate]    = objData
            elif (type(objData) == Product):
                self.tableProduct[idToUpdate]   = objData
            else:
                raise Exception("Error!")

            return True
        except:
            return False


    def list(self, recordType: tableTypes) -> bool:
        """ Public method to list all registers of a table """
        try:
            if recordType == tableTypes.CUSTOMER or recordType == tableTypes.SELLER:
                # Table header
                print("#" + "-" * 88)
                print("# List of customers ")
                print("#" + "-" * 88)
                print("|%4s|%20s|%25s|%10s|%11s|%11s|" % ("ID", "Full name", "Address", "Phone", "Birthdate",
                        ("Registered" if recordType == tableTypes.CUSTOMER else "Admission")))
                print("#" + "-" * 88)

                # Depending on record type read corresponding table
                if recordType == tableTypes.CUSTOMER:
                    for recordIdx in self.tableCustomer:
                        print("|%4s%s" % (str(recordIdx), self.tableCustomer[recordIdx]))
                elif recordType == tableTypes.SELLER:
                    for recordIdx in self.tableSeller:
                        print("|%4s%s" % (str(recordIdx), self.tableSeller[recordIdx]))
            elif recordType == tableTypes.PRODUCT:
                # Table header
                print("#" + "-" * 70)
                print("# List of Products ")
                print("#" + "-" * 70)
                print("|%4s|%25s|%25s|%12s|" % ( "ID", "Product", "Manufacturer", "Price"))
                print("#" + "-" * 70)

                # Iterate over all items in the table (dictionary)
                for recordIdx in self.tableProduct:
                    print("|%4s%s" % (str(recordIdx), self.tableProduct[recordIdx]))
            elif recordType == tableTypes.SALE:
                print("Listing sales... To be done!")
            else:
                raise Exception("Error!")

            return True
        except:
            return False

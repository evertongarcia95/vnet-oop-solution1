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
        #try:
        if (type(objData) == Customer):
            self.tableCustomer[self.__nextID(self.tableCustomer)]   = objData
        elif (type(objData) == Seller):
            self.tableSeller[self.__nextID(self.tableSeller)]       = objData
        elif (type(objData) == Product):
            self.tableProduct[self.__nextID(self.tableProduct)]     = objData
        #except:
        #    return False
        #finally:
        #    return True


    def remove(self, objData) -> bool:
        """ Public method to remove a register from the database """
        try:
            pass
        except:
            return False
        finally:
            return True


    def update(self, objData) -> bool:
        """ Public method to modify a register of the database """
        try:
            pass
        except:
            return False
        finally:
            return True


    def list(self, recordType: tableTypes) -> bool:
        """ Public method to list all registers of a table """
        try:
            if recordType == tableTypes.CUSTOMER:
                # Table header
                print("#" + "-" * 79)
                print("# List of customer ")
                print("#" + "-" * 79)
                print("|%4s|%10s|%10s|%15s|%10s|%10s|%11s| " % ("ID","Name","Surname","Address","Phone","Birthdate","Registered"))
                for record in self.tableCustomer:
                    print(record)
            elif recordType == tableTypes.SELLER:
                print("reading seller")
            elif recordType == tableTypes.PRODUCT:
                print("reading product")
            elif recordType == tableTypes.SALE:
                print("reading sale")
            else:
                raise Exception("Error!")
        except:
            return False
        finally:
            return True

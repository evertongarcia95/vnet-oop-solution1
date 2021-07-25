"""
Views of the application

* CRUD ::
    Create
    Read
    Update
    Delete

* List ::

* 
"""

from datetime import datetime
from typing import final

from .database.database import Database, tableTypes

from .database.models.people import Customer, Seller
from .database.models.product import Product


# Instance of temporary database object
appDatabase = Database()

"""
if (obj != None):
    # Exibe os ingredientes
    print(objBolo)

    # Preparando o bolo...
    print("#" + "-" * 79)
    print("# Preparando o bolo... ")
    print("#" + "-" * 79)
    objBolo.prepararBolo()

    # Pronto!
    print("#" + "-" * 79)
    print(f"# Peso total to bolo: {objBolo.pesoTotalBolo() / 1000:.3f} Kg.")
    print("#" + "-" * 79)
"""

def createRecord(recordType: tableTypes) -> bool:
    """ Function to handle addition of records to the table """
    #try:
    if recordType == tableTypes.CUSTOMER:
        print("#" + "-" * 79)
        print("Adding customer")
        print("#" + "-" * 79)

        custName    = str(input("Name: ") or "Joao")
        custSurname = str(input("Surname: ") or "da Silva")
        custAddress = str(input("Address: ") or "R dos Andradas 1011")
        custPhone   = int(input("Phone number: ") or "0119992993")
        print("Birth date:")
        custBirth   = datetime(int(input("\tyear:") or "2021"), int(input("\tmonth:") or "1"), int(input("\tday:") or "1"))

        # Object instance
        objCustomer = Customer(custName, custSurname, custAddress, custPhone, custBirth, datetime.today())

        # Adding to the database
        appDatabase.add(objCustomer)

    elif recordType == tableTypes.SELLER:
        print("adding seller")
    elif recordType == tableTypes.PRODUCT:
        print("adding product")
    elif recordType == tableTypes.SALE:
        print("adding sale")
    else:
        raise Exception("Error!")
    #except:
    #    return False
    #finally:
    #    return True


def readRecord(recordType: tableTypes) -> bool:
    """ Function to read records of the table """
    try:
        if recordType == tableTypes.CUSTOMER:
            print("reading customer")
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


def updateRecord(recordType: tableTypes) -> bool:
    """ Function to update records of the table """
    try:
        if recordType == tableTypes.CUSTOMER:
            print("updating customer")
        elif recordType == tableTypes.SELLER:
            print("updating seller")
        elif recordType == tableTypes.PRODUCT:
            print("updating product")
        elif recordType == tableTypes.SALE:
            print("updating sale")
        else:
            raise Exception("Error!")
    except:
        return False
    finally:
        return True


def deleteRecord(recordType: tableTypes) -> bool:
    """ Function to delete records from the table """
    try:
        if recordType == tableTypes.CUSTOMER:
            print("deleting customer")
        elif recordType == tableTypes.SELLER:
            print("deleting seller")
        elif recordType == tableTypes.PRODUCT:
            print("deleting product")
        elif recordType == tableTypes.SALE:
            print("deleting sale")
        else:
            raise Exception("Error!")
    except:
        return False
    finally:
        return True


def listAllRecords(recordType: tableTypes) -> bool:
    """ Function to list all records in the table """
    #try:
    return appDatabase.list(recordType)
    #except:
    #    return False

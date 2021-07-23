"""
Models of people related databases
"""
import datetime 

class Person:
    """ Base class of type Person """
    def __init__(self, ID_Person: int, name: str, surname: str, address: str, phoneNumber: int, birthDate: datetime.date) -> None:
        self.ID_Person: int             = ID_Person
        self.name: str                  = name
        self.surname: str               = surname
        self.address: str               = address
        self.phoneNumber: int           = phoneNumber
        self.birthDate: datetime.date   = birthDate

    def setFullName(self, name: str = None, surname: str = None) -> None:
        """ Update full name of this person """
        if name:    self.name       = name
        if surname: self.surname    = surname

    def getFullName(self) -> str:
        """ Obtain full name of this person """
        return self.name + " " + self.surname

    def setAddress(self, address: str) -> None:
        """ Update the address of this person """
        self.address = address
    
    def getAddress(self) -> str:
        """ Obtain the address of this person """
        return self.address

    def setPhoneNumber(self, phoneNumber: int) -> None:
        """ Update the phone number of this person """
        self.phoneNumber = phoneNumber

    def getPhoneNumber(self) -> str:
        """ Obtain the phone number of this person """
        return self.phoneNumber

    def setBirthDate(self, birthDate: datetime.date) -> None:
        """ Update the birth date of this person """
        self.birthDate = birthDate
    
    def getBirthDate(self) -> datetime.date:
        """ Obtain the birth date of this person """
        return self.birthDate


class Customer(Person):
    """ Extended class of type Customer based on Person """
    def __init__(self, ID_Person: int, name: str, surname: str, address: str, phoneNumber: int, birthDate: datetime.date , ID_Customer: int, RegisterDate: datetime.date) -> None:
        super (). __init__ (ID_Person, name, surname, address, phoneNumber, birthDate)
        self.ID_Customer: int               = ID_Customer
        self.RegisterDate: datetime.date    = RegisterDate

    def setRegisterDate(self, RegisterDate: datetime.date) -> None:
        """ Update the register date of this customer """
        self.RegisterDate = RegisterDate

    def getRegisterDate(self) -> datetime.date:
        """ Obtain the register date of this customer """
        return self.RegisterDate


class Seller(Person):
    """ Extended class of type Seller based on Person """
    def __init__(self, ID_Person: int, name: str, surname: str, address: str, phoneNumber: int, birthDate: datetime.date , ID_Seller: int, AdmissionDate: datetime.date) -> None:
        super (). __init__ (ID_Person, name, surname, address, phoneNumber, birthDate)
        self.ID_Seller: int = ID_Seller
        self.AdmissionDate: datetime.date = AdmissionDate

    def setAdmissionDate(self, AdmissionDate: datetime.date) -> None:
        """ Update the admission date of this customer """
        self.AdmissionDate = AdmissionDate

    def getAdmissionDate(self) -> datetime.date:
        """ Obtain the admission date of this customer """
        return self.AdmissionDate

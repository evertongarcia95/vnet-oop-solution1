"""
Models of people related databases
"""
import datetime 

class Person(object):
    """ Base class of type Person """
    def __init__(self, name: str, surname: str, address: str, phoneNumber: int, birthDate: datetime.date) -> None:
        self.name: str                  = name
        self.surname: str               = surname
        self.address: str               = address
        self.phoneNumber: int           = phoneNumber
        self.birthDate: datetime.date   = birthDate

    def __str__(self) -> str:
        return "|%10s|%10s|%15s|%10s|%10s| " % (str(self.name),str(self.surname),str(self.address),str(self.phoneNumber),str(self.birthDate))

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
    def __init__(self, name: str, surname: str, address: str, phoneNumber: int, birthDate: datetime.date , registerDate: datetime.date) -> None:
        super (). __init__ (name, surname, address, phoneNumber, birthDate)
        self.registerDate: datetime.date = registerDate

    def __str__(self) -> str:
        return "|%s|%11s| " % (super().__str__(), str(self.registerDate))

    def setRegisterDate(self, registerDate: datetime.date) -> None:
        """ Update the register date of this customer """
        self.registerDate = registerDate

    def getRegisterDate(self) -> datetime.date:
        """ Obtain the register date of this customer """
        return self.registerDate


class Seller(Person):
    """ Extended class of type Seller based on Person """
    def __init__(self, name: str, surname: str, address: str, phoneNumber: int, birthDate: datetime.date , admissionDate: datetime.date) -> None:
        super (). __init__ (name, surname, address, phoneNumber, birthDate)
        self.admissionDate: datetime.date = admissionDate

    def setAdmissionDate(self, admissionDate: datetime.date) -> None:
        """ Update the admission date of this customer """
        self.admissionDate = admissionDate

    def getAdmissionDate(self) -> datetime.date:
        """ Obtain the admission date of this customer """
        return self.admissionDate


"""
Models of people related databases
"""
import datetime 

class Person(object):
    """ Base class of type Person """
    def __init__(self, name: str, surname: str, address: str, phoneNumber: int, birthDate: datetime.date) -> None:
        self.__name: str                  = name
        self.__surname: str               = surname
        self.__address: str               = address
        self.__phoneNumber: int           = phoneNumber
        self.__birthDate: datetime.date   = birthDate

    def __str__(self) -> str:
        return "|%20s|%25s|%10s|%11s|" % (str(self.getFullName()),
            str(self.getAddress()),
            str(self.getPhoneNumber()),
            str(self.getBirthDate().strftime("%m/%d/%Y")))

    def setName(self, name: str) -> None:
        """ Update name of this person """
        self.__name = name

    def getName(self) -> str:
        """ Obtain name of this person """
        return self.__name

    def setSurname(self, surname: str) -> None:
        """ Update surname of this person """
        self.__surname = surname

    def getSurname(self) -> str:
        """ Obtain surname of this person """
        return self.__surname

    def setFullName(self, name: str = None, surname: str = None) -> None:
        """ Update full name of this person """
        if name:    self.__name       = name
        if surname: self.__surname    = surname

    def getFullName(self) -> str:
        """ Obtain full name of this person """
        return self.__name + " " + self.__surname

    def setAddress(self, address: str) -> None:
        """ Update the address of this person """
        self.__address = address
    
    def getAddress(self) -> str:
        """ Obtain the address of this person """
        return self.__address

    def setPhoneNumber(self, phoneNumber: int) -> None:
        """ Update the phone number of this person """
        self.__phoneNumber = phoneNumber

    def getPhoneNumber(self) -> int:
        """ Obtain the phone number of this person """
        return self.__phoneNumber

    def setBirthDate(self, birthDate: datetime.date) -> None:
        """ Update the birth date of this person """
        self.__birthDate = birthDate
    
    def getBirthDate(self) -> datetime.date:
        """ Obtain the birth date of this person """
        return self.__birthDate


class Customer(Person):
    """ Extended class of type Customer based on Person """
    def __init__(self, name: str, surname: str, address: str, phoneNumber: int, birthDate: datetime.date , registerDate: datetime.date) -> None:
        super (). __init__ (name, surname, address, phoneNumber, birthDate)
        self.__registerDate: datetime.date = registerDate

    def __str__(self) -> str:
        return "%s%11s|" % (super().__str__(), str(self.getRegisterDate().strftime("%m/%d/%Y")))

    def setRegisterDate(self, registerDate: datetime.date) -> None:
        """ Update the register date of this customer """
        self.__registerDate = registerDate

    def getRegisterDate(self) -> datetime.date:
        """ Obtain the register date of this customer """
        return self.__registerDate


class Seller(Person):
    """ Extended class of type Seller based on Person """
    def __init__(self, name: str, surname: str, address: str, phoneNumber: int, birthDate: datetime.date , admissionDate: datetime.date) -> None:
        super (). __init__ (name, surname, address, phoneNumber, birthDate)
        self.__admissionDate: datetime.date = admissionDate

    def __str__(self) -> str:
        return "%s%11s|" % (super().__str__(), str(self.getAdmissionDate().strftime("%m/%d/%Y")))

    def setAdmissionDate(self, admissionDate: datetime.date) -> None:
        """ Update the admission date of this customer """
        self.__admissionDate = admissionDate

    def getAdmissionDate(self) -> datetime.date:
        """ Obtain the admission date of this customer """
        return self.__admissionDate


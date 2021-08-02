"""
Models of people related databases
"""
import datetime

class Person :
     def __init__(self, ID_Person: int, Name: str, Surname: str, Address: str, PhoneNumber: int, BirthDate: datetime.date) -> None:
         self.ID_Person: int = ID_Person
         self.Name: str = Name
         self.Surname: str = Name
         self.Address: str = Address
         self.PhoneNumber: int = PhoneNumber
         self.BirthDate: datetime.date = Birthdate

     def setName(self, name: str , Surname: str) -> None:
        self.Name = Name
        self.Surname = Surname
    
     def getName(self) -> str:
         return self.Name + " " + self.Surname

     def setAddress(self, Address: str) -> None:
         self.Address = Address

     def getAddress(self) -> str:
         return self.Address

     def setPhoneNumber(self, PhoneNumber: int) -> None:
         self.PhoneNuber = PhoneNumber

     def getPhoneNumber(self) -> int:
         return self.PhoneNumber

     def setBirthDate(self, BirthDate: datetime.date ) -> None:
        self.Birthdate = BirthDate

     def getBirthDate(self) -> datetime.date:
         return self.BirthDate



class Custumer (Person):
     def __init__(self, ID_Custumer: int, RegisterDate: date ) -> None:
        self.ID_Custumer: int = ID_Custumer
        self.RegisterDate: date = RegisterDate

     def setRegisterDate(self, RegisterDate: date) -> None:
         self.RegisterDate = RegisterDate

     def getRegisterDate(self) -> date:
         return self.RegisterDate


class Seller (person):
     def __init__(self, ID_Seller: int, AdmissionDate: date ) -> None:
        self.ID_Seller: int = ID_Seller
        self.AdimissionDate: date = AdimissionDate

     def setAdmissionDate(self, AdmissionDate: date) -> None:
         self.AdmissionDate = AdimissionDate

     def getAdmissionDate(self) -> date:
         return self.AdmissionDate
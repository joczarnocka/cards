from tkinter import N
from faker import Faker

fake = Faker()

class BaseContact:
    def __init__(self, firstname, surname, private_phone, email) -> None:
        self.firstname = firstname
        self.surname = surname
        self.private_phone = private_phone
        self.email = email
        self._name_length = len(f"{self.firstname} {self.surname}")
     
    def __str__(self) -> str:
         return f"{self.firstname} {self.surname}: {self.email}"

    def contact(self) -> None:
        #print( f"Kontaktuję się z {self.firstname} {self.surname}")
        print(f"Wybieram numer {self.private_phone} i dzwonię do {self.firstname} {self.surname}.")

    @property
    def name_length(self):
        return self._name_length

class BusinessContact(BaseContact):

    def __init__(self, role, company, business_phone, *args, **kwargs) -> None:
        super().__init__( *args, **kwargs)
        self.role = role
        self.company = company
        self.busines_phone = business_phone

    def __str__(self) -> str:
         return f"{self.firstname} {self.surname}: {self.email} ( {self.role}, {self.company})"

    def contact(self) -> None:
        print(f"Wybieram numer {self.busines_phone} i dzwonię do {self.firstname} {self.surname}.")


def giveCard() -> BaseContact:
    firstname = fake.first_name()
    surname = fake.last_name()
    phone = fake.phone_number()
    email= f"{firstname}.{surname}@{fake.domain_name()}"
    return BaseContact(firstname, surname, phone, email)


def create_contacts(card_type, card_number) -> list:
    res_list = []
    for i in range(card_number):
        firstname = fake.first_name()
        surname = fake.last_name()
        phone = fake.phone_number()
        email= f"{firstname}.{surname}@{fake.domain_name()}"
        if card_type == "base":
            card = BaseContact(firstname, surname, phone, email)
        else:
            role = fake.job()
            phone2 = fake.phone_number()
            company = fake.company()
            card = BusinessContact(role,company,phone2,firstname, surname,phone, email)
        res_list.append(card) 
    return res_list

if __name__ == "__main__":
    # bc = BusinessContact("engineer","IBM", "+48 030349534","John","Smith","+48 0324934290", "john.smith@ibm.com")
    # print(bc.name_length)
    # card_list = [ContactCard("Adam","Adamski","CompanyA","adam@gmail.com"),
    #              ContactCard("Bartek","Bartkowski","CompanyB","bartek@gmail.com"),
    #              ContactCard("Cezary","Cezarski","CompanyC","cezary@gmail.com"),
    #              ContactCard("Damian","Damiano","CompanyD","damian@gmail.com"),
    #              ContactCard("Edward","Edwardski","CompanyE","edward@gmail.com"),
    #             ]

    # card_list = [giveCard(), giveCard(), giveCard(), giveCard()]


    # for card in card_list:
    #     print(card)

    # by_firstname = sorted(card_list, key=lambda card: card.firstname)
    # by_surname = sorted(card_list, key=lambda card: card.surname)
    # by_email = sorted(card_list, key=lambda card: card.email)

    # #print(by_surname) # jak zrobic drukowanie listy
    # for card in by_email:
    #     print(card)

    # print(by_email[0].name_length)  

    cards_list = create_contacts("business", 4)

    for card in cards_list:
        print(card)
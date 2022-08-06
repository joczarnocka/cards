from tkinter import N
from faker import Faker

fake = Faker()

class BaseContact:
    def __init__(self, firstname, surname, company, email) -> None:
        self.firstname = firstname
        self.surname = surname
        self.company = company
        self.email = email
        self._name_length = len(f"{self.firstname} {self.surname}")
     
    def __str__(self) -> str:
         return f"{self.firstname} {self.surname}: {self.email}"

    def contact(self) -> None:
        print( f"Kontaktuję się z {self.firstname} {self.surname}")

    @property
    def name_length(self):
        return self._name_length


    

def giveCard() -> BaseContact:
    firstname = fake.first_name()
    surname = fake.last_name()
    company = fake.company()
    email= f"{firstname}.{surname}@{fake.domain_name()}"
    return BaseContact(firstname, surname, company, email)



if __name__ == "__main__":
    # card_list = [ContactCard("Adam","Adamski","CompanyA","adam@gmail.com"),
    #              ContactCard("Bartek","Bartkowski","CompanyB","bartek@gmail.com"),
    #              ContactCard("Cezary","Cezarski","CompanyC","cezary@gmail.com"),
    #              ContactCard("Damian","Damiano","CompanyD","damian@gmail.com"),
    #              ContactCard("Edward","Edwardski","CompanyE","edward@gmail.com"),
    #             ]

    card_list = [giveCard(), giveCard(), giveCard(), giveCard()]


    for card in card_list:
        print(card)

    by_firstname = sorted(card_list, key=lambda card: card.firstname)
    by_surname = sorted(card_list, key=lambda card: card.surname)
    by_email = sorted(card_list, key=lambda card: card.email)

    #print(by_surname) # jak zrobic drukowanie listy
    for card in by_email:
        print(card)

    print(by_email[0].name_length)   
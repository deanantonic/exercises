"""
Contact List
Step 1

Write a "Contact" class in which you can store contact information with name and email.
Step 2

Store the Contact objects (which you instantiate) in a list, which is a class attribute, called all_contacts.
Step 3

Write a reset_contacts class method, which can clean (clean and not re-instantiate!) the all_contacts list.
Step 4

Write a "Supplier" class, which is inherited from the Contact class.
Step 5

Write an "order" method for the Supplier, which has a single argument - a string. Store these orders in a class attribute, called all_orders, in a dictionary, where the key is the supplier email (because it's usually unique), and the value is a list of the orders. So if you add multiple orders, it will be added to the list of that key.
Step 6

Write a "ContactList" class, which extends the built-in Python "list" (list class, which you use everyday, https://docs.python.org/3.5/library/stdtypes.html#list). Use this custom ContactList as the storage of all_contacts.
Step 7

Write a "search" method for the ContactList, which can search in the name of the stored contacts and find the matching names (not with exact match, it should also work for matching parts). The input argument is a string (what we search), and the output is a list of all matching Contact objects.
Step 8

Write a "longest_name" method for the ContactList, which can gives back the longest name from the stored contacts.
"""


class ContactList(list):

    def search(self, string):
        return [elem for elem in self if string in elem.name]

    def longest_name(self):
        try:
            longest = self[0].name
        except Exception:
            return None
        else:
            for element in self:
                if len(element.name) > len(longest):
                    longest = element.name
        return longest


class Contact:

    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        cls.all_contacts = ContactList()


class Supplier(Contact):

    all_orders = {}

    def __init__(self, name, email):
        Contact.__init__(self, name, email)
        Supplier.all_orders[self.email] = []

    def order(self, string):
        Supplier.all_orders[self.email].append(string)


contact = Contact("Dean", "dean@gmail.com")
contact1 = Contact("Some Body", "somebody@example.net")
contact3 = Contact("Elek Benedek", "elek.benedek@example.net")
supplier = Supplier("Supp Lier", "suplier@example.net")
supplier1 = Supplier("Supp Lier", "suplier@example.net")
supplier1.order("CD Player")
supplier1.order("DVD Player")
print contact3.all_contacts.search("Elek")
print Contact.all_contacts.longest_name()

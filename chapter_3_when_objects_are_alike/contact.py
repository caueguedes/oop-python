class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print(
            "If this were a real system  we would send"
            f"'{order}' order to '{self.name}'"
        )


c = Contact("Some body", "somebody@example.net")
s = Supplier("Sup plier", "supplier@example.net")

print(c.name, c.email, s.name, s.email)  # Some Body somebody@example.net Sup Plier supplier@example.net

c.all_contacts  # [<__main__.Contact object at 0xb7375ecc>, <__main__.Supplier object at 0xb7375f8c>]
c.order("I need pliers")  # AttributeError: 'Contact' object has no attribute 'order'
s.order("I need pliers")  # If this were a real system we would send 'I need pliers' order to 'Sup Plier '

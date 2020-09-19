class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


# Mixin
class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)
        # Add e-mail logic here


class EmailableContact(Contact, MailSender):
    pass


e = EmailableContact("John Smith", "jsmith@example.net")
Contact.all_contacts  # [ < __main__.EmailableContact object at 0xb7205fac >]

e.send_mail("Hello, test e-mail here")  # Sending mail to jsmith @ example.net

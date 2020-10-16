class Email:
    def __init__(self, from_addr, to_addr, subject, message):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self._message = message

    def message(self):
        return self._message


email = Email(
    "a@example.com",
    "b@example.com",
    "You have Mail!",
    "Here's some mail for you!",
)

formatted = f"""
From: <{email.from_addr}>
To: <{email.to_addr}>
Subject: <{email.subject}>

{email.message()}"""

print(formatted)

f"['a' for a in range(5)]"
"['a' for a in range(5)]"
f"{'yes' if True else 'no'}"  # 'yes'

class Person(object):
    def __init__(self, firstname: str, lastname: str, email: str, phone: str) -> None:
        self.firstname = str(firstname)
        self.lastname = str(lastname)
        self.email = str(email)
        self.phone = str(phone)

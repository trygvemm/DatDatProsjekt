
#from msilib.schema import Class
class User:

    def __init__(self, mail, password, firstName, lastName):
        self.mail = mail
        self.password = password
        self.firstName = firstName
        self.lastName = lastName

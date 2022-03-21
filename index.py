from tokenize import String
from User import User
from Post import Post
import SQLindex


def start():
    print("Velkommen til Kaffeapp\n")
    loglag = input("Logg inn skriv 1 \nLag bruker skriv 2")

    if loglag == "1":
        logIn()
    elif loglag == "2":
        makeUser()


def makeUser():
    mail = input("Skriv inn mail: ")
    firstName = input("Skriv inn fornavn: ")
    lastName = input("Skriv inn etternavn: ")
    password = input("Skriv inn passord: ")
    user = User(mail, password, firstName, lastName)
    SQLindex.insert_user(user)
    logIn()


def logIn():
    print("LOGG INN:")
    mail = input("Skriv inn mail: ")
    password = input("Skriv inn passord: ")
    dbPassword = SQLindex.get_password(mail)

    if (dbPassword != None):
        if(dbPassword[0] == password):
            print("Du er logget inn")
        else:
            print("Feil passord")
            logIn()
    else:
        print(f"Ingen brukere med mail: {mail}")
        start()


start()

from tokenize import String
from User import User
from Post import Post
import SQLindex

userid = None


def start():
    print("Velkommen til Kaffeapp\n")
    loglag = input("Logg inn: 1 \nLag bruker: 2\n")
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
            menu()
        else:
            print("Feil passord")
            logIn()
    else:
        print(f"Ingen brukere med mail: {mail}")
        start()

def menu():
    choose = input("Lag Post: 1\nSe post: 2\nToppliste smakt flest kaffe: 3\nMest for pengene: 4\nFinn i beskrivelse: 5\nLand: 6\n")
    if choose == "1":
        post()
    else:
        print("under dev")
        menu()


start()

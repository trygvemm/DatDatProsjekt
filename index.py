from tokenize import String
from datetime import date
from User import User
from Post import Post
import SQLindex

# tid
now = date.today()
date = now.strftime("%d-%m-%Y")

userid = None

def start():
    print("-----Velkommen til Kaffeapp-----\n")
    loglag = input("Logg inn: 1 \nLag bruker: 2\nSKIP: 3")
    if loglag == "1":
        logIn()
    elif loglag == "2":
        makeUser()
    elif loglag == "3":
        userid = 4
        print("Du er logget inn som SUNIL")
        menu()
    else:
        print("feil input")
        start()

def makeUser():
    print("----------LAG BRUKER----------")
    mail = input("Skriv inn mail: ")
    firstName = input("Skriv inn fornavn: ")
    lastName = input("Skriv inn etternavn: ")
    password = input("Skriv inn passord: ")
    user = User(mail, password, firstName, lastName)
    SQLindex.insert_user(user)
    logIn()

def logIn():
    print("----------LOGG INN----------")
    mail = input("Skriv inn mail: ")
    password = input("Skriv inn passord: ")
    dbPassword = SQLindex.get_password(mail)

    if (dbPassword != None):
        if(dbPassword[0] == password):
            print("Du er logget inn")
            userid = mail
            menu()
        else:
            print("Feil passord")
            logIn()
    else:
        print(f"Ingen brukere med mail: {mail}")
        start()

def menu():
    print("----------MENY----------")
    choose = input(
        "Lag Post: 1\nSe post: 2\nToppliste smakt flest kaffe: 3\nMest for pengene: 4\nFinn i beskrivelse: 5\nLand: 6\n")
    if choose == "1":
        makePost()
    if choose == "2":
        seePost()
    else:
        print("under dev")
        menu()

def makePost():
    print("----------LAG POST----------")
    coffee = input("Skriv inn kaffenavn: ")
    roastery = input("Skriv inn brennerinavn: ")
    score = input("Skriv inn score (1-10): ")
    note = input("Skriv inn beskrivelse: ")

    coffeeid = SQLindex.getCoffeeID(coffee, roastery)
    if coffeeid != None:
        post = Post(userid, coffeeid, note, score, date)
        SQLindex.insert_post(post)
        print("Suksess, du har laget en post")
        menu()
    else:
        print("Feil verdier for kaffenavn eller kaffebrenneri")
        makePost()

def seePost():
    print("----------SE POST----------")

start()

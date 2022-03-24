from tokenize import String
from datetime import date
from User import User
from Post import Post
from prettytable import PrettyTable
import SQLindex

# tid
now = date.today()
date = now.strftime("%d-%m-%Y")

userid = ""


def start():
    print("-----Velkommen til Kaffeapp-----\n")
    loglag = input("Logg inn: 1 \nLag bruker: 2\nSkip: 3\n")
    if loglag == "1":
        logIn()
    elif loglag == "2":
        makeUser()
    elif loglag == "3":
        userid = "Bharat@gmail.com"
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
    print(userid)
    choose = input(
        "Lag Post: 1\nListe over hvem som har smakt flest kaffer: 2\nBest kaffe for pengene: 3\nSøk i beskrivelse: 4\nLand: 5\nEXIT: 6\n")
    if choose == "1":
        makePost()
    elif choose == "2":
        topList()
    elif choose == "3":
        mostValue()
    elif choose == "4":
        search()
    elif choose == "5":
        search_not_washed()
    elif choose == "6":
        exit()
    else:
        print("under dev")
        menu()


def makePost():
    print("----------LAG POST----------")
    userid = 'Bharat@gmail.com'
    coffee = input("Skriv inn kaffenavn: ")
    roastery = input("Skriv inn brennerinavn: ")
    score = int(input("Skriv inn score (1-10): "))
    note = input("Skriv inn beskrivelse: ")

    coffeeid = SQLindex.getCoffeeID(coffee, roastery)
    if coffeeid != None:
        post = Post(userid, coffeeid[0], note, score, date)
        SQLindex.insert_post(post)
        print("Suksess, du har laget en post")
        menu()
    else:
        print("Feil verdier for kaffenavn eller kaffebrenneri")
        makePost()


def seePost():
    print("----------SE POST----------")


def makePost():
    print("----------LAG POST----------")
    userid = 'per@gmail.com'
    coffee = input("Skriv inn kaffenavn: ")
    roastery = input("Skriv inn brennerinavn: ")
    score = int(input("Skriv inn score (1-10): "))
    note = input("Skriv inn beskrivelse: ")

    coffeeid = SQLindex.getCoffeeID(coffee, roastery)
    if coffeeid != None:
        post = Post(userid, coffeeid[0], note, score, date)
        SQLindex.insert_post(post)
        print("Suksess, du har laget en post")
        menu()
    else:
        print("Feil verdier for kaffenavn eller kaffebrenneri")
        makePost()


def topList():
    print("----------TOPPLISTE----------")
    # så langt i år????????
    list = SQLindex.get_mostcoffee()
    PT = PrettyTable()
    PT.field_names = ["Fornavn", "Antall smakt kaffer"]
    for i in range(len(list)):
        PT.add_row(list[i])
    print(PT)
    menu()


def mostValue():
    print("----------BEST KAFFE FOR PENGENE----------")
    list = SQLindex.get_mostvalue()
    PT = PrettyTable()
    PT.field_names = ["Brennerinavn", "Kaffenavn",
                      "Pris/kg", "Gjennomsnittscore", "Pris/poeng"]
    for i in range(len(list)):
        PT.add_row(list[i])
        # print(list[i])
    print(PT)
    menu()


def search():
    print("----------SØK ETTER KAFFEBESKRIVELSE----------")
    usr = input("Søk: ")
    list = SQLindex.get_search(usr)
    PT = PrettyTable()
    PT.field_names = ["Kaffenavn", "Brennerinavn"]
    for i in range(len(list)):
        PT.add_row(list[i])
    print(PT)
    menu()


4


def search_not_washed():
    print("----------Kaffer fra Colombia og Rwanda hvor bønnene ikke er vasket ----------")
    country = input("Colombia eller Rwanda? ")
    list = SQLindex.get_search_not_washed(country)
    PT = PrettyTable()
    PT.field_names = ["Brennerinavn", "Kaffenavn"]
    for i in range(len(list)):
        PT.add_row(list[i])
        # print(list[i])
    print(PT)
    menu()


start()

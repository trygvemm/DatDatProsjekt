#Datamodellering og databasesystemer TDT4145 Prosjekt delinnlevering 2
#Gruppe 168 - Trygve Myhr, Bharat Premkumar, Sunil Sharma

#import moduler
from tokenize import String
from datetime import date
from User import User
from Post import Post
from prettytable import PrettyTable
import SQLindex

#Hente tid idag
now = date.today()
date = now.strftime("%d-%m-%Y")

userid = ""

#Startmeny
def start(userid):
    print("-----Velkommen til Kaffeapp-----")
    loglag = input("Logg inn: 1 \nLag bruker: 2\nSkip: 3\n")
    if loglag == "1":
        logIn(userid)
    elif loglag == "2":
        makeUser(userid)
    elif loglag == "3":
        userid = "test@test.com"
        print("Du er logget inn som test")
        menu(userid)
    else:
        errormsg(1)
        start(userid)

#Registrere bruker
def makeUser(userid):
    print("----------LAG BRUKER----------")
    mail = input("Skriv inn mail: ")
    firstName = input("Skriv inn fornavn: ")
    lastName = input("Skriv inn etternavn: ")
    password = input("Skriv inn passord: ")
    user = User(mail, password, firstName, lastName)
    try:
        SQLindex.insert_user(user)
    except:
        errormsg(2)
    start(userid)

#Logg inn
def logIn(userid):
    print("----------LOGG INN----------")
    mail = input("Skriv inn mail: ")
    password = input("Skriv inn passord: ")
    dbPassword = SQLindex.get_password(mail)
    if (dbPassword != None):
        if(dbPassword[0] == password):
            print(f"Du er logget inn som: {mail} ")
            userid = mail
            menu(userid)
        else:
            errormsg(3)
            logIn(userid)
    else:
        errormsg(4)
        start(userid)

#Hovedmeny
def menu(userid):
    print("----------MENY----------")
    choose = input(
        "Lag Post: 1\nListe over hvem som har smakt flest kaffer: 2\nBest kaffe for pengene: 3\nSøk i beskrivelse: 4\nSøk etter uvaskede kaffer fra Land: 5\nLOGG UT: 6\n")
    if choose == "1":
        makePost(userid)
    elif choose == "2":
        topList(userid)
    elif choose == "3":
        mostValue(userid)
    elif choose == "4":
        search(userid)
    elif choose == "5":
        search_not_washed(userid)
    elif choose == "6":
        exit()
    else:
        errormsg(1)
        menu(userid)

#Lag en post
def makePost(userid):
    print("----------LAG POST----------")
    coffee = input("Skriv inn kaffenavn: ")
    roastery = input("Skriv inn brennerinavn: ")
    score = input("Skriv inn score (1-10): ")
    try:
        score = int(score)
    except:
        errormsg(6)
        makePost(userid)
    if(score > 10 or score < 0):
        errormsg(6)
        makePost(userid)
    note = input("Skriv inn beskrivelse: ")

    coffeeid = SQLindex.getCoffeeID(coffee, roastery)
    if coffeeid != None:
        post = Post(userid, coffeeid[0], note, score, date)
        SQLindex.insert_post(post)
        print("Suksess, du har laget en post")
        menu(userid)
    else:
        errormsg(5)
        menu(userid)

#Skriv ut topplist for hvem som har smakt flest unike kaffer
def topList(userid):
    print("----------TOPPLISTE----------")
    list = SQLindex.get_mostcoffee()
    PT = PrettyTable()
    PT.field_names = ["Fornavn", "Antall smakt kaffer"]
    for i in range(len(list)):
        PT.add_row(list[i])
    print(PT)
    menu(userid)

#Skriv ut liste over hvilken kaffe som gir mest for pengene
def mostValue(userid):
    print("----------BEST KAFFE FOR PENGENE----------")
    list = SQLindex.get_mostvalue()
    PT = PrettyTable()
    PT.field_names = ["Brennerinavn", "Kaffenavn",
                      "Pris/kg", "Gjennomsnittscore", "Pris/poeng"]
    for i in range(len(list)):
        PT.add_row(list[i])
    print(PT)
    menu(userid)

#Søk i beskrivelsen laget av en bruker eller kaffebrenneri
def search(userid):
    print("----------SØK ETTER KAFFEBESKRIVELSE----------")
    usr = input("Søk: ")
    list = SQLindex.get_search(usr)
    PT = PrettyTable()
    PT.field_names = ["Kaffenavn", "Brennerinavn"]
    for i in range(len(list)):
        PT.add_row(list[i])
    print(PT)
    menu(userid)

#søk etter kaffer som ikke er vasket fra land
def search_not_washed(userid):
    print("----------SØK ETTER UVASKEDE BØNNER FRA LAND----------")
    country = input("Søk etter land: ")
    list = SQLindex.get_search_not_washed(country)
    PT = PrettyTable()
    PT.field_names = ["Brennerinavn", "Kaffenavn"]
    for i in range(len(list)):
        PT.add_row(list[i])
    print(PT)
    menu(userid)

#Skriv ut error
def errormsg(n):
    print("ERROR:")
    if n == 1:
        print("Feil input")
    elif n == 2:
        print("Denne mailen finnes:(")
    elif n == 3:
        print("Feil passord")
    elif n == 4:
        print("Ingen brukere med denne mailen")
    elif n == 5:
        print("Feil verdier for kaffenavn eller kaffebrenneri")
    elif n == 6:
        print("Skriv et tall mellom 1-10")

#Kjør applikasjonen
start(userid)

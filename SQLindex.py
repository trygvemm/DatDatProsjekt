from importlib import import_module
from multiprocessing import connection
from User import User
from Post import Post

import sqlite3


def chk_conn(conn):
    try:
        conn.cursor()
        return True
    except Exception as ex:
        return False


connection = sqlite3.connect('coffee.db')
cursor = connection.cursor()
print(chk_conn(connection))

#cursor.execute("INSERT INTO tabelnavn VALUES (tall, 'tekst', 'tekst')")
#cursor.execute("UPDATE tabellnavn SET verdi = '' WHERE ID = tall")
#cursor.execute("DELETE FROM tabellnavn WHERE ID = tall")

def insert_user(user):
    with connection:
        cursor.execute("INSERT INTO User VALUES (:mail, :password, :firstName, :lastName)", {
                       'mail': user.mail, 'password': user.password, 'firstName': user.firstName, 'lastName': user.lastName})

def insert_post(post):
    with connection:
        cursor.execute("INSERT INTO Post (mail, coffeeID, note, score, date) VALUES (:mail, :coffeeID, :note, :score, :date)", {
        'mail': "Sunil@gmail.com", 'coffeeID': post.coffeeID, 'note': post.note, 'score': post.score, 'date': post.date})

def insert_post(post):
    with connection:
        cursor.execute("INSERT INTO Post (mail, coffeeID, note, score, date) VALUES (:mail, :coffeeID, :note, :score, :date)", {
            'mail': post.mail[0], 'coffeeID': post.coffeeID[0], 'note': post.note[0], 'score': post.score[0], 'date': post.date})

def get_password(mail):
    cursor.execute(
        "SELECT password FROM User WHERE mail=:mail", {'mail': mail})
    return cursor.fetchone()

def getCoffeeID(Cname, Rname):
    cursor.execute(
        "SELECT coffeeID From Coffee WHERE coffeeName = :Cname AND roasteryID = (SELECT roasteryID from CoffeeRoastery WHERE name = :name)", {'Cname': Cname, 'name': Rname})
    return cursor.fetchone()

def get_mostcoffee():
    cursor.execute(
        "SELECT User.firstName, COUNT(DISTINCT Post.coffeeID) AS total from Post Inner join User on Post.mail = User.mail group by User.firstName ORDER BY total DESC;")
    return cursor.fetchall()

def get_mostvalue():
    cursor.execute(
        "SELECT CoffeeRoastery.name, Coffee.coffeeName, Coffee.priceKG, AVG(Post.score), Coffee.priceKG/AVG(Post.score) AS prisperpoeng from Post INNER JOIN Coffee ON Coffee.coffeeID = Post.coffeeID INNER JOIN CoffeeRoastery ON CoffeeRoastery.roasteryID = Coffee.roasteryID GROUP BY Coffee.coffeeName ORDER BY prisperpoeng;")
    return cursor.fetchall()

def get_search(search):
    cursor.execute(
        "SELECT DISTINCT Coffee.coffeeName, CoffeeRoastery.name FROM Coffee INNER JOIN CoffeeRoastery ON Coffee.roasteryID = CoffeeRoastery.roasteryID INNER JOIN Post ON Post.coffeeID = Coffee.coffeeID WHERE Post.note LIKE :search OR Coffee.description LIKE :search", {'search': '%'+search+'%'})
    return cursor.fetchall()

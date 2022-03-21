from importlib import import_module
from multiprocessing import connection
#from User import User
#from Post import Post

import sqlite3
connection = sqlite3.connect('coffee.db')
cursor = connection.cursor()

#cursor.execute("INSERT INTO tabelnavn VALUES (tall, 'tekst', 'tekst')")
#cursor.execute("UPDATE tabellnavn SET verdi = '' WHERE ID = tall")
#cursor.execute("DELETE FROM tabellnavn WHERE ID = tall")


def insert_user(user):
    with connection:
        cursor.execute("INSERT INTO User VALUES (:mail, :password, :firstName, :lastName)", {
                       'mail': user.mail, 'password': user.password, 'firstName': user.firstName, 'lastName': user.lastName})


def get_user_by_name(lastNamename):
    cursor.execute(
        "SELECT * FROM User WHERE lastName=:lastName", {'lastName': lastNamename})
    return cursor.fetchall()


def get_password(mail):
    print("kjør a")
    cursor.execute(
        "SELECT password FROM User WHERE mail=:mail", {'mail': mail})
    return cursor.fetchone()


def update_post(user, pay):
    with connection:
        cursor.execute("""UPDATE employees SET pay = :pay
                    WHERE firstName = :firstName AND lastName = :lastName""",
                       {'firstName': user.firstName, 'lastName': user.lastName, 'pay': pay})


def remove_user(user):
    with connection:
        cursor.execute("DELETE from employees WHERE firstName = :firstName AND lastName = :lastName",
                       {'firstName': user.firstName, 'lastName': user.lastName})

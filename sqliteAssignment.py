from multiprocessing import connection
import sqlite3
connection = sqlite3.connect('C:/Users/Gabe/Desktop/testDatabase.db')


c = connection.cursor()
c.execute("CREATE TABLE IF NOT EXISTS People(FirstName TEXT, LastName TEXT, Age INT)")


c.execute("INSERT INTO People VALUES('Jon', 'Doe', 42)")
connection.commit()
#need to commit all changes to tables
#sqlite doesn't like it when you use " " for data entry. this may create errors

connection.close()
#no memory leaks :) same thing as closing a file

#with sqlite3.connect("C:/Users/Gabe/Desktop/testDatabase.db") as connection:
#You should use this to simplify the code. with this, you no longer need to .commit()
#this will auto close the DB as well. many advantages in using this including fixing some errors
#use .commit() for immediate results


#connection.sqlite3.connect(':memory:')
#This will make a temp DB

with sqlite3.connect('C:/Users/Gabe/Desktop/testDatabase.db') as connection:
    c = connection.cursor() #cursor is a function. it NEEDS '()'
    c.executescript("""DROP TABLE IF EXISTS People2;
                        CREATE TABLE People2(FirstName TEXT, LastName TEXT, Age INT);
                        INSERT INTO People2 VALUES('Jack', 'Black', 23);""")
    #executescript() will allow you to make a multi-line script. This improves readability
    
    Persons2 = (('Luke', 'Skywalker', 45), ('Darth', 'Vader', 63))
    c.executemany('INSERT INTO People2 VALUES(?,?,?)', Persons2)
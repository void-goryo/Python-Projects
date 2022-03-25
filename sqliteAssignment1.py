
import sqlite3

#get data from user
firstName = input('Enter your first name: ')
lastName = input('Enter your last name: ')
age = int(input('Enter your age: '))
personData = (firstName, lastName, age)

with sqlite3.connect('testDatabase.db') as connection:
    c = connection.cursor()
    c.execute('DROP TABLE IF EXISTS People')
    c.execute("CREATE TABLE People (Fname TEXT, Lname TEXT, Age INT)")
    line = "INSERT INTO People VALUES ('" + firstName +"', '"+ lastName +"', "+ str(age) + ")"
                                           #'string',           'string',        int
    c.execute(line)

    c.execute('INSERT INTO People VALUES(?,?,?)', personData)
    #I like this a lot better 

    c.execute('SELECT * FROM People')
    for row in c.fetchall():
        print(row)

    c.execute('SELECT * FROM People')
    while True:
        row = c.fetchone()
        if row is None: 
            break
        print(row)
import sqlite3


#connection = sqlite3.connect(':memory:')   you could use this, but you would have to close and commit at the end

names = [('Jean-Baptiste Zorg', 'Human', 122),
            ('Korben Dallas', 'Meat Popsicle', 100),
            ("Ak'not", 'Mangalore', -5)]




with sqlite3.connect(':memory:') as connection:     #use this instead
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS Roster;")
    c.executescript("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
    c.executemany('INSERT INTO Roster (Name, Species, IQ) VALUES (?,?,?);', names)

    c.execute("SELECT * FROM Roster")
    for row in c.fetchall():
        print(row)

    c.execute("UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas'")

    c.execute('SELECT * FROM Roster WHERE Name = "Korben Dallas"')
    for row in c.fetchall():
        print(row)
    




#c.executescript("""INSERT INTO Roster(Name, Species, IQ) VALUES('Jean-Baptiste Zorg', 'Human', 122);
#                                    ('Korben Dallas', 'Meat Popsicle', 100);
#                                    ('Ak'''''not', 'Mangalore', -5);""")
#This was a good try
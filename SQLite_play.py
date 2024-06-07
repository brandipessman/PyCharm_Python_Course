import sqlite3

db = sqlite3.connect("books-collection.db") # create a database if one doesn't exist

cursor = db.cursor() #creat a cursor which will control our database

#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, "
               # keywords in all caps, 
               # CREATE TABLE creates a new table in the database, 
               # books is the name of the table, 
               # inside () are the columns, 
               # lowercase is name
               # PRIMARY KEY uniquely identifies that record in the table
            #"title varchar(250) NOT NULL UNIQUE, "
               # title column takes a variable-length string up to 250 characters
               # NOT NULL means it cannot be left empty
               # UNIQUE means it cannot match any other records
            #"author varchar(250) NOT NULL, "
            #"rating FLOAT NOT NULL)")

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K.Rowling', '9.3')")

db.commit() # don't forget to commit changes
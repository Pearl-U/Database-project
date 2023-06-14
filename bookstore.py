''' 
Level 2 - T6: Capstone Project 1 (Database)
Author: KP Useh

Create a program that can be used by a bookstore clerk. The program
should allow the clerk to:
add new books to the database
update book information
delete books from the database
search the database to find a specific book.
'''
# Import SQLite3
import sqlite3
# Allow for scenario where db does not exist
db = None
try:
    # Create a database called ebookstore_db
    db = sqlite3.connect('ebookstore_db')
    cursor = db.cursor()  # Get a cursor object

    # Create a table called books
    cursor.execute('''
    CREATE TABLE books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT,
                   	Qty INTEGER)''')
    # Save changes to database
    db.commit()


    # Add the following Book data
    id1 = 3001
    title1 = 'A tale of two Cities'
    author1 = 'Charles Dickens'
    qty1 = 30

    id2 = 3002
    title2 = "Harry Potter and the Philosopher's Stone"
    author2 = 'J.K Rowling'
    qty2 = 40

    id3 = 3003
    title3 = "The Lion, the Witch and the Wardrobe"
    author3 = 'C.S Lewis'
    qty3 = 25

    id4 = 3004
    title4 = "The Lord of the Rings"
    author4 = 'J,R.R Tolkien'
    qty4 = 37

    id5 = 3005
    title5 = "Alice in Wonderland"
    author5 = 'Lewis Carroll'
    qty5 = 12

    # Create list of book data called books_
    books_ = [(id1,title1,author1, qty1),(id2,title2,author2, qty2),(id3,title3,author3, qty3),(id4,title4,author4, qty4),(id5,title5,author5, qty5)]

    # Insert books_ list into book Table
    cursor.executemany('''INSERT INTO books(id, Title, Author, Qty) VALUES(?,?,?,?)''', books_)
    print('All books stored in table')
    print('books Table')
    print('-'*20)

    # Save changes to database
    db.commit()
    # Create a function to add a new book
    def enter_book():
        id = int(input("Enter id: "))
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        qty = int(input("Enter book quantity: "))
    
        cursor.execute('''INSERT INTO books(id, Title, Author, Qty) VALUES(?,?,?,?)''', (id,title,author,qty))
        print('New book inserted in books table')
    
    # Create function to update a book's quantity
    def update_book():
        id = int(input("Enter book id to update: "))
        qty = int(input("Enter updated quantity: "))
        cursor.execute('''UPDATE books SET qty = ? WHERE id = ?''', (qty, id))
        print('\nBook id %d data has been updated' %id)   
    
    # Create a function to delete a book
    def delete_book():
        id = int(input("Enter book id to delete: "))
        cursor.execute('''DELETE FROM books WHERE id = ? ''', (id,))
        print('\nBook id %d data has been deleted' %id) 

    # Create a function to search for a book
    def search_book():
        id = int(input('Enter book id: '))
        cursor.execute('''SELECT * FROM books WHERE id = ?''', (id,))
        book = cursor.fetchone()
        print(book)

    # Display the original books table
    cursor.execute('''SELECT * FROM books''')
    for row in cursor:
        print('id:{0} - {1}, {2}, quantity: {3}'.format(row[0], row[1], row[2], row[3]))
    print('\n')

    # Save changes to database
    db.commit() 

    menu = ""
    # Create a menu that allows the user to
    # enter, update, delete or search for a book
    # Allow user to exit the program when done.
    while menu != "0":
        menu = input('''What would you like to do - 
    1 - Enter book
    2 - Update book
    3 - Delete book
    4 - Search books
    0 - Exit \n''')

        if menu == "1":
            enter_book()
        
        elif menu == "2":
            update_book()
  
        elif menu == "3":
            delete_book()

        elif menu == "4":
            search_book()

        elif menu == "0":
            print("Goodbye")
        else:
            print("Oops - incorrect input")

    cursor.execute('''DROP TABLE books''')
    print('\nbooks table deleted!')

    # Save changes to database
    db.commit()

except FileNotFoundError:
    print("The file you are trying to open does not exist")

    # Reverse change is something goes wrong
    db.rollback()
    
finally:
    if db is not None:
        # Close the db connection
        db.close()
        print('Connection to database closed\n')



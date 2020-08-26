import sqlite3

database = 'contact_book.db'

# Connect to DB
try:
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    print('Successfully connected to database')

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    cursor.close()
    print("SQLite Database Version is: ", record)    
except sqlite3.Error as error:
    print('Error while connecting: ', error)
    exit()

try:
    connection.execute(
    '''CREATE TABLE IF NOT EXISTS CONTACT(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, ADDRESS TEXT, PHONE_NUMBER CHAR(15) NOT NULL, EMAIL CHAR(20)); '''
    )
except sqlite3.Error as error:
    print(error)

def insert_contact(connection):
    name = input('Name: ')
    address = input('Address: ')
    phone_number= input('Phone Number: ')
    email = input('Email: ')
    query = '''INSERT INTO CONTACT (name, address, phone_number, email) VALUES ('{}', '{}', '{}', '{}')'''.format(name, 
        address, phone_number, email)
    try:
        connection.execute(query)
        connection.commit()
        print('Successfully added entry')
    except sqlite3.Error as error:
        print('Error: ', error)

def delete_contact(connection):
    name = input('Name to delete: ')
    test_query = "SELECT * FROM CONTACT WHERE name='{}'".format(name)
    query = "DELETE FROM CONTACT WHERE name='{}'".format(name)
    cursor = connection.cursor()
    cursor.execute(test_query)
    if cursor.fetchone():
        cursor.execute(query)
        connection.commit()
        print('Successfully deleted')
    else:
        print('Contact does not exist!')

def show_contact(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM CONTACT')
    records = cursor.fetchall()
    for row in records:
        print("{:20} {:20} {:20} {:20}".format(row[1], row[2], row[3], row[4]))
    cursor.close()

print('''Choice: 
    1. Insert contact
    2. Delete contact
    3. Show contact''')

try:
    while True:
        choice = input('Select: ')
        if choice == '1':
            insert_contact(connection)
        elif choice == '2':
            delete_contact(connection)
        elif choice == '3':
            show_contact(connection)
        else:
            pass
except KeyboardInterrupt:
    print('\nExiting..')
    connection.close()
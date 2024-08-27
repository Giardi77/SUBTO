import sqlite3
import bcrypt
import getpass

def PreparaDatabase() -> tuple:
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('./Database/users.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create the users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()

    return conn, cursor

def RegisterUser(username, password, conn, cursor) -> tuple:
    # Hash the password
    HashedPassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        # Insert the new user into the database
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, HashedPassword))
        conn.commit()
        print(f'User {username} registered successfully.')
        return True
    except sqlite3.IntegrityError:
        print(f'Username {username} is already taken.')
        return False

    # Close the connection when done
    conn.close()


def LoginUser(username, password, conn, cursor) -> tuple:
    # Retrieve the user record from the database
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()

    if result:
        StoredPassword = result[0]
        # Check the hashed password
        if bcrypt.checkpw(password.encode('utf-8'), StoredPassword):
            print(f'User {username} logged in successfully.')
            return True
        else:
            print('Incorrect password.')
            return False
    else:
        print('Username not found. You can register with the -r flag')
        return False

    # Close the connection when done
    conn.close()

def Auth(Register) -> tuple:
    conn, cursor = PreparaDatabase()
    passwordMatch = True
    
    if Register:
        username = input('Username: ')
        while passwordMatch:
            password = getpass.getpass("password: ")
            repeated = getpass.getpass("confirm password: ")

            if password == repeated:
                result = RegisterUser(username, password, conn, cursor)
                passwordMatch = False
                return result, username
            else:
                print('passwords do not match, try again')

    else:
        username = input('Username: ')
        password = getpass.getpass("password: ")
        result = LoginUser(username, password, conn, cursor)
        return result, username
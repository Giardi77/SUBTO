import sqlite3
import bcrypt
import getpass
import tabulate

def PreparaDatabase() -> tuple:
    conn = sqlite3.connect('./Database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS scans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        target TEXT NOT NULL,
        FOREIGN KEY (username) REFERENCES users(username)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS scan_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        scan_id INTEGER NOT NULL,
        subdomain TEXT NOT NULL,
        fingerprint TEXT NOT NULL,
        vulnerable BOOLEAN NOT NULL,
        FOREIGN KEY (scan_id) REFERENCES scans(id)
    )
    ''')

    conn.commit()
    return conn, cursor

def RegisterScan(username, target ) -> int:
    conn, cursor = PreparaDatabase()
    cursor.execute('INSERT INTO scans (username, target) VALUES (?, ?)', (username, target))
    conn.commit()

    scan_id = cursor.lastrowid
    conn.close()
    return scan_id

def GetUserScans(username) -> None:
    conn, cursor = PreparaDatabase()
    cursor.execute('SELECT id, target FROM scans WHERE username = ?', (username,))
    scans = cursor.fetchall()

    if scans:
        print(f'Scans for user {username}:')
    
        print(tabulate.tabulate(scans,headers=['id','target'], tablefmt='grid'))
    else:
        print(f'No scans found for user {username}.')
    conn.close()

def RegisterScanResult(scan_id, subdomain, fingerprint, vulnerable) -> None:
    conn, cursor = PreparaDatabase()

    cursor.execute('''
    INSERT INTO scan_results (scan_id, subdomain, fingerprint, vulnerable)
    VALUES (?, ?, ?, ?)
    ''', (scan_id, subdomain, fingerprint, vulnerable))
    conn.commit()
    conn.close()

def GetScanResults(scan_id) -> None:
    conn, cursor = PreparaDatabase()

    cursor.execute('''
    SELECT subdomain, fingerprint, vulnerable
    FROM scan_results
    WHERE scan_id = ?
    ''', (scan_id,))
    
    scans = cursor.fetchall()

    if scans:
        print(f'Scan results for Scan ID {scan_id}:')
        print(tabulate.tabulate(scans,headers=['subdomain', 'fingerprint', 'vulnerable'], tablefmt='grid'))
    else:
        print(f'No results found for Scan ID {scan_id}.')
    conn.close()

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
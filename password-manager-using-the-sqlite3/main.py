# password_manager.py

import sqlite3
import hashlib
import secrets

# Connect to the database
conn = sqlite3.connect('passwords.db')

# Create the passwords table if it doesn't exist
conn.execute('''CREATE TABLE IF NOT EXISTS passwords
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             website TEXT NOT NULL,
             username TEXT NOT NULL,
             password TEXT NOT NULL);''')

# Define a function to add a new password to the database
def add_password(website, username, password):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Insert the new password into the database
    conn.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)", (website, username, hashed_password))
    conn.commit()
    print("Password added successfully!")

# Define a function to retrieve a password from the database
def get_password(website):
    # Retrieve the password hash from the database
    cursor = conn.execute("SELECT password FROM passwords WHERE website=?", (website,))
    result = cursor.fetchone()

    if result:
        hashed_password = result[0]
        print("Enter master password:")
        master_password = input()

        # Hash the master password and compare it to the stored password hash
        if hashlib.sha256(master_password.encode('utf-8')).hexdigest() == hashed_password:
            print("Password for", website, "is:", secrets.token_urlsafe(16))
        else:
            print("Incorrect master password.")
    else:
        print("No password found for", website)

# Define a function to print all passwords in the database
def print_passwords():
    cursor = conn.execute("SELECT * FROM passwords")
    for row in cursor:
        print("Website:", row[1])
        print("Username:", row[2])
        print("Password:", row[3])
        print()

# Main loop
while True:
    print("Select an option:")
    print("1. Add a new password")
    print("2. Retrieve a password")
    print("3. Print all passwords")
    print("4. Quit")

    choice = input()

    if choice == "1":
        website = input("Enter website name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        add_password(website, username, password)
    elif choice == "2":
        website = input("Enter website name: ")
        get_password(website)
    elif choice == "3":
        print_passwords()
    elif choice == "4":
        break
    else:
        print("Invalid option.")

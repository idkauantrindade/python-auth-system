import mysql.connector
import bcrypt

DB_NAME = "auth_system"
TABLE_NAME = "users"

def init_db():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    cursor = db.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    db.close()

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=DB_NAME
    )
    cursor = db.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(60) NOT NULL
        )
    """)
    db.commit()
    db.close()

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=DB_NAME
    )

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    db = get_connection()
    cursor = db.cursor()

    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
    if cursor.fetchone():
        print("User already exists!")
        db.close()
        return

    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, hashed_password.decode())
    )
    db.commit()
    db.close()
    print("Account created successfully!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()

    if not result:
        print("User not found!")
        db.close()
        return

    stored_hash = result[0]
    if bcrypt.checkpw(password.encode(), stored_hash.encode()):
        print("Login successful!")
    else:
        print("Incorrect password!")

    db.close()

def main():
    init_db()

    while True:
        print("\n1 - Register")
        print("2 - Login")
        print("3 - Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
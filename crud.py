import psycopg2
from dbconnectcopy import connect

def create():
    print("creating in database...")
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES ('user1', 'password123');")
        db_version = cursor.fetchone()
        print(f"username is: {db_version[0]}")
        cursor.close()
        connection.close()
    else:
        print("Connection to database failed.")

def read():
    print("reading database...")
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT username FROM users1;")
        db_version = cursor.fetchone()
        print(f"username is: {db_version[0]}")
        cursor.close()
        connection.close()
    else:
        print("Connection to database failed.")

def update():
    print("updating in database...")
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET password = 'newpassword123' WHERE username = 'user1';")
            # UPDATE table_name
            # SET column1 = value1, column2 = value2, ...
            # WHERE condition;
        db_version = cursor.fetchone()
        print(f"username is: {db_version[0]}")
        cursor.close()
        connection.close()
    else:
        print("Connection to database failed.")

def delete():
    print("Deleting in database...")
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM users WHERE username = 'user1';")
            # DELETE FROM table_name
            # WHERE condition;
        db_version = cursor.fetchone()
        print(f"username is: {db_version[0]}")
        cursor.close()
        connection.close()
    else:
        print("Connection to database failed.")



### Testing
def testing():
    print("Deleting to database...")
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT username FROM users1;")
        db_version = cursor.fetchone()
        print(f"username is: {db_version[0]}")
        cursor.close()
        connection.close()
    else:
        print("Connection to database failed.")

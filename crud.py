# import psycopg2
from dbconnectcopy import connect

def create(user, password):
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO users (username, password) VALUES ('{user}', '{password}');")
        connection.commit()
        cursor.close()
    else:
        print("Connection to database failed.")
    connection.close()

def read(user, password):
    confirmation = True
    connection = connect()
    print("reading database...")
    if connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM users WHERE username='{user}' AND password ='{password}';")
        sqlinjection = cursor.fetchone()
        cursor.close()
        if sqlinjection != None:
            print("user exist.")
        else:
            print("user not exist.")
            confirmation = False
    else:
        print("Connection to database failed.")
    connection.close()
    return confirmation

def update(olduser, newuser):
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute(f"UPDATE users SET username = '{newuser}' WHERE username = '{olduser}';")
        connection.commit()
        cursor.close()
    else:
        print("Connection to database failed.")
    connection.close()

def delete(user):
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM users WHERE username = '{user}';")
        connection.commit()
        cursor.close()
    else:
        print("Connection to database failed.")
    connection.close()


def userexist(user):
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT username FROM users WHERE username='{user}';")
        sqlinjection = cursor.fetchone()
        cursor.close()
        if sqlinjection != None:
            return True
        else:
            return False
    else:
        print("Connection to database failed.")
    connection.close()


### Testing
# read('jj','0')
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

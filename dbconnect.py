import psycopg2

def connect():
    print("Connecting to database...")
    # Connection parameters
    host = "127.0.0.1"
    database = "users"
    user = "jj"
    password = "1"
    port="5433"

    try:
        # Establish connection
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        cursor = connection.cursor()

        # # Print PostgreSQL version
        # cursor.execute("SELECT version();")
        # db_version = cursor.fetchone()
        # print(f"Connected to: {db_version[0]}")

        # Print PostgreSQL version
        cursor.execute("SELECT username FROM users1;")
        db_version = cursor.fetchone()
        print(f"username is: {db_version[0]}")

    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
    finally:
        # Clean up
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection closed.")

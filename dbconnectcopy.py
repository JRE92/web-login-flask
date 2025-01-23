import psycopg2

def connect():
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

    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return

    return connection

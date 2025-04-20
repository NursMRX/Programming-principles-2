import psycopg2

DB_PARAMS = {
    "host": "localhost",
    "database": "snake_game",
    "user": "postgres",
    "password": "12345678",
    "port": "5432"
}

def connect_db():
    return psycopg2.connect(**DB_PARAMS)


conn = connect_db()


with conn.cursor() as cur:
    cur.execute("")
    
    rows = cur.fetchall()

    print("Содержимое таблицы users:")
    for row in rows:
        print(row)


conn.close()

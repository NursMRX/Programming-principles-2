import psycopg2


conn = psycopg2.connect(
    dbname=" snake_game",
    user="postgres",
    password="clay0xRoot",
    host="localhost"
)

def execute_query(query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)



with conn.cursor() as cur:
    cur.execute("SELECT * FROM users;")    
    
    
    
    
    rows = cur.fetchall()
    for row in rows:
        print(row)


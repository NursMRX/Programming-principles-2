import psycopg2

conn = psycopg2.connect(
    dbname="snake_game",  # или любая другая существующая БД
    user="postgres",
    password="your_password",
    host="localhost"
)

cur = conn.cursor()

cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
databases = cur.fetchall()

print("Список баз данных:")
for db in databases:
    print("-", db[0])

cur.close()
conn.close()

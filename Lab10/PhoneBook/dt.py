import psycopg2

conn = psycopg2.connect(
    dbname="phonebook",  # укажи нужную БД
    user="postgres",
    password="your_password",
    host="localhost"
)

cur = conn.cursor()

cur.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public';
""")

tables = cur.fetchall()

print("Список таблиц:")
for table in tables:
    print("-", table[0])

cur.close()
conn.close()

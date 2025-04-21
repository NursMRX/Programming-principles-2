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


def delete_user_score(username):
    conn = connect_db()
    if not conn:
        return

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM user_scores WHERE username = %s", (username,))
                deleted_rows = cur.rowcount
                print(f"Deleted {deleted_rows} row(s) from user_scores for username '{username}'.")
    except psycopg2.Error as e:
        print("Error executing delete query:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    username = input("Enter username to delete score for: ").strip()
    delete_user_score(username)
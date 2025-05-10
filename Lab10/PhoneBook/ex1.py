import psycopg2
import csv
from psycopg2 import Error

db_params = {
    "host": "localhost",
    "database": "phonebook",
    "user": "postgres",
    "password": "12345678",
}

def connect_db():
    """Establish a database connection."""
    return psycopg2.connect(**db_params)

def create_table(conn):
    """Create the Phonebook table if it doesn't exist."""
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Phonebook (
                surname VARCHAR(255),
                name VARCHAR(255),
                number VARCHAR(20),
                PRIMARY KEY (surname)
            );
        """)
        conn.commit()

def insert_manual(conn):
    """Insert data manually."""
    while True:
        print("Type 'enter' to add more data or 'stop' to break:")
        mode = input().lower()
        if mode == "stop":
            break
        if mode != "enter":
            print("Invalid input. Please type 'enter' or 'stop'.")
            continue

        surname = input("Enter surname: ").strip()
        name = input("Enter name: ").strip()
        number = input("Enter phone number: ").strip()

        # Validate inputs
        if not surname or not name or not number:
            print("All fields are required.")
            continue
        if not number.replace("+", "").replace("-", "").isdigit():
            print("Phone number must contain only digits, '+' or '-'.")
            continue

        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO Phonebook (surname, name, number) VALUES (%s, %s, %s)",
                    (surname, name, number)
                )
                conn.commit()
                print("Record added successfully.")
        except Error as e:
            print(f"Error inserting data: {e}")
            conn.rollback()

def insert_from_csv(conn):
    """Insert data from a CSV file."""
    while True:
        print("Want to insert data from CSV file? (yes/no):")
        mode = input().lower()
        if mode == "no":
            break
        if mode != "yes":
            print("Invalid input. Please type 'yes' or 'no'.")
            continue

        filename = input("Enter the name of the CSV file (without .csv): ").strip() + ".csv"
        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                next(reader, None)  # Skip header, if present
                with conn.cursor() as cur:
                    for row in reader:
                        if len(row) != 3:
                            print(f"Skipping invalid row: {row}")
                            continue
                        cur.execute(
                            "INSERT INTO Phonebook (surname, name, number) VALUES (%s, %s, %s)",
                            row
                        )
                    conn.commit()
                    print("Data inserted from CSV successfully.")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Error as e:
            print(f"Error inserting data from CSV: {e}")
            conn.rollback()

def update_record(conn):
    """Update a record in the Phonebook."""
    while True:
        print("Type 'update' to update data or 'stop' to break:")
        mode = input().lower()
        if mode == "stop":
            break
        if mode != "update":
            print("Invalid input. Please type 'update' or 'stop'.")
            continue

        display_table(conn)
        surname = input("Enter surname to update: ").strip()
        print("What do you want to change? (name/number):")
        field = input().lower()
        if field not in ["name", "number"]:
            print("Invalid field. Please choose 'name' or 'number'.")
            continue

        new_value = input(f"Enter new {field}: ").strip()
        if not new_value:
            print("New value cannot be empty.")
            continue
        if field == "number" and not new_value.replace("+", "").replace("-", "").isdigit():
            print("Phone number must contain only digits, '+' or '-'.")
            continue

        try:
            with conn.cursor() as cur:
                cur.execute(
                    f"UPDATE Phonebook SET {field} = %s WHERE surname = %s",
                    (new_value, surname)
                )
                conn.commit()
                if cur.rowcount == 0:
                    print(f"No record found with surname '{surname}'.")
                else:
                    print(f"Record updated successfully.")
        except Error as e:
            print(f"Error updating data: {e}")
            conn.rollback()

def delete_record(conn):
    """Delete a record from the Phonebook."""
    while True:
        print("Want to delete some data? (yes/no):")
        mode = input().lower()
        if mode == "no":
            break
        if mode != "yes":
            print("Invalid input. Please type 'yes' or 'no'.")
            continue

        display_table(conn)
        surname = input("Enter surname to delete: ").strip()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM Phonebook WHERE surname = %s",
                    (surname,)
                )
                conn.commit()
                if cur.rowcount == 0:
                    print(f"No record found with surname '{surname}'.")
                else:
                    print(f"Record deleted successfully.")
        except Error as e:
            print(f"Error deleting data: {e}")
            conn.rollback()

def display_table(conn):
    """Display all records in the Phonebook."""
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Phonebook")
            rows = cur.fetchall()
            if not rows:
                print("Phonebook is empty.")
            else:
                print("\nPhonebook Records:")
                print("Surname | Name | Number")
                print("-" * 40)
                for row in rows:
                    print(f"{row[0]} | {row[1]} | {row[2]}")
                print()
    except Error as e:
        print(f"Error fetching data: {e}")

def main():
    """Main function to run the phonebook application."""
    try:
        with connect_db() as conn:
            create_table(conn)
            print("Phonebook Application")
            print("--------------------")
            insert_manual(conn)
            insert_from_csv(conn)
            update_record(conn)
            delete_record(conn)
            print("\nFinal Phonebook State:")
            display_table(conn)
    except Error as e:
        print(f"Database connection error: {e}")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    finally:
        print("Closing application.")

if __name__ == "__main__":
    main()
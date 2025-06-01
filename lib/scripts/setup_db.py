import sqlite3

def get_connection():
    return sqlite3.connect('address_book.db')

def setup_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS addresses (
        id INTEGER PRIMARY KEY,
        location TEXT NOT NULL,
        contact_id INTEGER,
        FOREIGN KEY(contact_id) REFERENCES contacts(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS phone_numbers (
        id INTEGER PRIMARY KEY,
        number TEXT NOT NULL,
        contact_id INTEGER,
        FOREIGN KEY(contact_id) REFERENCES contacts(id)
    )
    """)

    conn.commit()

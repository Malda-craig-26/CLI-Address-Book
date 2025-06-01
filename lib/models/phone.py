from db.connection import get_connection


class PhoneNumber:
    def __init__(self, number, contact_id, id=None):
        self.id = id
        self.number = number
        self.contact_id = contact_id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id:
            cursor.execute("UPDATE phone_numbers SET number = ? WHERE id = ?", (self.number, self.id))
        else:
            cursor.execute("INSERT INTO phone_numbers (number, contact_id) VALUES (?, ?)", (self.number, self.contact_id))
            self.id = cursor.lastrowid
        conn.commit()
        return self

    def delete(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM phone_numbers WHERE id = ?", (self.id,))
        conn.commit()

    @classmethod
    def find_by_contact_id(cls, contact_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM phone_numbers WHERE contact_id = ?", (contact_id,))
        return [cls(row["number"], row["contact_id"], row["id"]) for row in cursor.fetchall()]

from dataclasses import dataclass
import sqlite3
import csv


@dataclass
class Contact:
    name: str
    email: str
    phone: str


class SQLiteWrapper:

    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE contact_book(
                id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL UNIQUE
            );
            """
        )

    def select_with_limit(self):
        pass

    def order(self, value):
        pass

    def select_where(self, value):
        pass

    def select(self, value):
        pass

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    @staticmethod
    def export_from_csv(file_name):
        with open(file_name, 'r') as file:
            rows = csv.DictReader(file)
            data = [(row['id'], row['first_name'], row['last_name'], row['email'], row['phone']) for row in rows]
            return data

    def import_data_to_db(self, data):
        self.cursor.executemany(
            "INSERT INTO contact_book (id, first_name, last_name, email, phone) VALUES (?, ?, ?, ?, ?);",
            data
        )
        self.connection.commit()


if __name__ == '__main__':
    db_wrapper = SQLiteWrapper("contact_book.db")
    contacts_data = db_wrapper.export_from_csv("MOCK_DATA.csv")
    db_wrapper.create_table()
    db_wrapper.import_data_to_db(contacts_data)

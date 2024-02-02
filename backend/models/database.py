import psycopg

class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self, dbname, user, pwd, host='127.0.0.1', port='5433'):
        self.conn = psycopg.connect(f"dbname={dbname} user={user} password={pwd} host={host} port={port}")
        self.cursor = self.conn.cursor()

    def create_table_users(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                            (id SERIAL PRIMARY KEY,
                            first_name TEXT,
                            last_name TEXT,
                            email TEXT,
                            password TEXT,
                            birthday TIMESTAMP)''')

    def create_table_books(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books
                            (id SERIAL PRIMARY KEY,
                            title TEXT,
                            author TEXT,
                            cover TEXT)''')

    def create_table_rental(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS rental
                            (id SERIAL PRIMARY KEY,
                            bid INTEGER,
                            uid INTEGER,
                            rent_date TIMESTAMP)''')

    def get_users(self):
        pass

    def get_user(self, uid):
        pass

    def add_user(self, first_name, last_name, email, birthday, password):
        pass

    def update_user(self, user):
        pass

    def delete_user(self, uid):
        pass

    def get_books(self):
        pass

    def get_book(self, bid):
        pass

    def add_book(self, values):
        books = ",".join([f'({book[0]}, {book[1]}, {book[2]})' for book in values])
        self.cursor.execute(f'INSERT INTO books (title, author, cover) VALUES {books}')

    def update_book(self, book):
        pass
    
    def delete_book(self, bid):
        pass

    def get_rentals(self):
        pass

    def get_rental_by_uid(self, uid):
        pass

    def get_rental_by_bid(self, bid):
        pass

    def add_rental(self, bid, uid, data_time):
        pass

    def delete_rental(self, rid):
        pass
import psycopg

class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self, dbname, user, pwd, host='127.0.0.1', port='5433'):
        self.conn = psycopg.connect(f"dbname={dbname} user={user} password={pwd} host={host} port={port}")
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def create_table_users(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                            (id SERIAL PRIMARY KEY,
                            first_name TEXT,
                            last_name TEXT,
                            email TEXT,
                            password TEXT,
                            birthday TIMESTAMP)''')
        self.conn.commit()

    def create_table_books(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books
                            (id SERIAL PRIMARY KEY,
                            title TEXT,
                            description TEXT,
                            author TEXT,
                            cover TEXT,
                            year INTEGER)''')
        self.conn.commit()

    def create_table_rental(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS rental
                            (id SERIAL PRIMARY KEY,
                            bid INTEGER,
                            uid INTEGER,
                            rent_date TIMESTAMP)''')
        self.conn.commit()

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

    def get_books(self, start=0, limit=20):
        self.cursor.execute('SELECT * FROM books LIMIT %s OFFSET %s', (limit, start))
        return self.cursor.fetchall()
        
    def get_book(self, bid):
        self.cursor.execute('SELECT * FROM books WHERE id=%s', (bid))
        pass

    def add_books(self, values):
        self.cursor.executemany('''INSERT INTO books (title, author, cover, description, year) 
                                VALUES (%s, %s, %s, %s, %s)''', values)
        self.conn.commit()

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
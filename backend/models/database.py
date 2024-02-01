import psycopg

class Database:
    def __init__(self):
        self.conn
        self.cursor

    def connect(self, name, user, password, host='127.0.0.1', port='5433'):
        self.conn = psycopg.connect(f"dbname={name} user={user}")
        self.cursor = self.conn.cursor()
        pass

    def create_table_users(self):
        pass

    def create_table_books(self):
        pass

    def create_table_rental(self):
        pass

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

    def add_book(self, title, author, year):
        pass

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
import os
import csv
import env

from models.database import Database

db_name = os.environ.get('DB_NAME')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_user = os.environ.get('DB_USER')
db_pwd = os.environ.get('DB_PWD')

db = Database()
db.connect(dbname=db_name, user=db_user, pwd=db_pwd, host=db_host, port=db_port)

db.create_table_books()
db.create_table_users()
db.create_table_rental()

with open('temp/books.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, quoting=0)
    books = []
    for row in reader:
        row = [value.replace('"', '') for value in row]
        if row[4] != "" and row[6] != "" and row[7] != "":
            books.append((row[2], row[4], row[6], row[7], row[8]))
    books = books[1:]
    db.add_books(books)
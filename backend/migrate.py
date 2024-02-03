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

with open('temp/books.csv', 'r') as file:
    reader = csv.reader(file)
    books = [(row[2], row[4], row[6], row[8]) for row in reader]
    books = books[1:]
    print(books[10])
    db.add_books(books)
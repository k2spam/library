import os
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
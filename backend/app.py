import os
import env
from flask import Flask, jsonify

from models.database import Database


db_name = os.environ.get('DB_NAME')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_user = os.environ.get('DB_USER')
db_pwd = os.environ.get('DB_PWD')

db = Database()
db.connect(dbname=db_name, user=db_user, pwd=db_pwd, host=db_host, port=db_port)

app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({})

@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify({})

@app.route('/api/books', methods=['GET'])
def get_books():
    books = db.get_books()
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=False)
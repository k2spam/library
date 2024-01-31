from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({})

@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify({})

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify({})

if __name__ == '__main__':
    app.run(debug=False)
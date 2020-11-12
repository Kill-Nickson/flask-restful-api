from flask import Flask, jsonify, abort
import psycopg2


app = Flask(__name__)


@app.route('/')
def empty_homepage():
    return ''


@app.route('/users', methods=['GET'])
def get_users():
    with psycopg2.connect(dbname='postgres', user='postgres', password='postgres',
                          host='db', port=5432) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()
            if len(users) == 0:
                abort(404)
    return jsonify({'users': users})


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    with psycopg2.connect(dbname='postgres', user='postgres', password='postgres',
                          host='db', port=5432) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM users WHERE id = %s', (user_id, ))
            users = cursor.fetchall()
            if len(users) == 0:
                abort(404)
    return jsonify({'user': users[0]})


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    with psycopg2.connect(dbname='postgres', user='postgres', password='postgres',
                          host='db', port=5432) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM users WHERE id = %s', (user_id, ))
            users = cursor.fetchall()
            if len(users) == 0:
                abort(404)
            else:
                cursor.execute('DELETE FROM users WHERE id = %s', (user_id, ))
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

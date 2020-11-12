import psycopg2
from randomuser import RandomUser


def gen_hundred_users():
    user_list = RandomUser.generate_users(100, {'gender': 'male'})
    formatted_users = []
    for user in user_list:
        formatted_user = (user.get_first_name(),
                          user.get_last_name(),
                          user.get_age(),
                          user.get_gender(),
                          user.get_email())
        formatted_users.append(formatted_user)
    return formatted_users


def insert_users(users):
    with psycopg2.connect(dbname='postgres', user='postgres', password='postgres',
                          host='db', port=5432) as conn:
        with conn.cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id SERIAL PRIMARY KEY,
                            first_name varchar(30) NOT NULL,
                            last_name varchar(30) NOT NULL,
                            age int NOT NULL,
                            gender varchar(6) NOT NULL,
                            email varchar(50) NOT NULL
                            )''')

            records_list_template = ','.join(['%s'] * len(users))
            insert_query = 'INSERT INTO users (first_name, last_name, age, gender, email) values {}'.\
                format(records_list_template)
            cursor.execute(insert_query, users)


def main():
    formatted_users = gen_hundred_users()
    insert_users(formatted_users)


if __name__ == '__main__':
    main()

from sqlite3 import Error
import sqlite3
from time import ctime


def post_sql_query(sql_query):
    with sqlite3.connect('my.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(sql_query)
        except Error:
            pass
        result = cursor.fetchall()
        return result


def create_tables():
    users_query = '''CREATE TABLE IF NOT EXISTS USERS
                        (user_id INTEGER PRIMARY KEY NOT NULL,
                        username TEXT,
                        first_name TEXT,
                        last_name TEXT,
                        reg_date TEXT);'''

    post_sql_query(users_query)


def register_user(user, username, first_name, last_name):
    user_check_query = f'SELECT * FROM USERS WHERE user_id = {user};'
    user_check_data = post_sql_query(user_check_query)
    if not user_check_data:
        insert_to_db_query = f'INSERT INTO USERS (user_id, username, first_name,  last_name, reg_date) VALUES ' \
                             f'({user}, "{username}", "{first_name}", "{last_name}", "{ctime()}");'
        post_sql_query(insert_to_db_query)

def register_channel(channel_id, channel_name, channel_username, couunt):
    user_check_query = f'SELECT * FROM CHANNELS WHERE channel_id = {channel_id};'
    user_check_data = post_sql_query(user_check_query)
    if not user_check_data:
        insert_to_db_query = f'INSERT INTO CHANNELS (channel_id, channel_username, channel_name,  couunt) VALUES ' \
                             f'({channel_id}, "{channel_username}", "{channel_name}", "{couunt}");'
        post_sql_query(insert_to_db_query)
    else:
        a = '5'
        return a

def AllUserID():
    return post_sql_query('SELECT * FROM USERS')

def channel_ids():
    lis = []
    result = post_sql_query('SELECT channel_id FROM CHANNELS')
    for x in result:
        lis.append(x[0])
    return lis


create_tables()




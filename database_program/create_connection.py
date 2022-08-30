import psycopg2
from contextlib import contextmanager
from sqlite3 import Error
from faker import Faker


fake = Faker()


@contextmanager
def create_connection():
    """ create a database connection to a Postgres database """
    conn = None
    try:
        conn = psycopg2.connect(host='localhost', database='test', user='postgres', password='12345')
        yield conn
        conn.commit()
    except Error as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_context_connection(user_table):
    with create_connection() as conn:
        if conn is not None:
            create_table(conn, user_table)
        else:
            print("Error: can't create the database connection")


def select_data(user_select):
    with create_connection() as conn:
        if conn is not None:
            cur = conn.cursor()
            cur.execute(user_select)
            # print(cur.fetchall())
            return cur.fetchall()
            cur.close()
        else:
            print("Error: can't create the database connection")

"""
-------->
These functions get data from a database of words using SQLite queries.
-------->
By default:
 - The database is called 'database.db'
 - The table is called 'words'
-------->
"""

import logging
import sqlite3
from random import randint
from sqlite3 import OperationalError

logging.basicConfig(
    level=logging.DEBUG,
    filename='logs.log',
    format='%(asctime)s [%(levelname)s] |%(lineno)s| > %(message)s',
    filemode='w'
)

logger = logging.getLogger(__name__)
handler = logging.FileHandler(filename='logs.log')
logger.addHandler(handler)

conn = sqlite3.connect('database.db')

cur = conn.cursor()

try:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS words
        (id INTEGER NOT NULL PRIMARY KEY,
        eng_word TEXT NOT NULL UNIQUE,
        rus_word TEXT NOT NULL UNIQUE);
    """)
    logger.info('Connection established successfully...')
except OperationalError as error:
    logger.critical(f'Connection error to database! {error}')
    exit()


# Technical Functions

def get_new_id():
    try:
        result = cur.execute("""SELECT MAX(id) FROM words""")
        new_id = 0
        for i in result:
            new_id += i[0]
        return new_id + 1
    except OperationalError as error:
        logger.critical(error)


def db_len():
    """Returns database's len"""
    try:
        result = cur.execute("""
            SELECT *
            FROM words;
        """)
        db_len = 0
        for i in result:
            db_len += 1
        return db_len
    except OperationalError as error:
        logger.error(f'Something went wrong in the counting: {error}')

# Executing Functions


def insert_word(eng_word=None, rus_word=None):
    """Adds new word-pair to database"""
    if None in (eng_word, rus_word):
        logger.error('Incorrect args for `insert_word` func')
        return None
    db_id = get_new_id()
    try:
        cur.execute(f"""
            INSERT INTO words VALUES
            ('{db_id}', '{eng_word}', '{rus_word}');
        """)
        logger.info(f'Words {eng_word}:{rus_word} successfully added to db')
    except OperationalError as e:
        logger.error(f'OperationalError while inserting new values to db: {e}')


def delete_record(eng_word=None):
    """Deletes a record from database. Arg is ONLY in English!"""
    if eng_word is None:
        logger.error('Not expected `eng_word` to equal None')
        return None
    try:
        cur.execute(f"""
            DELETE FROM words WHERE eng_word = '{eng_word}';
        """)
    except OperationalError as error:
        logger.error(f'OperationalError while deleting from database: {error}')


def rus_from_eng(eng_word=None):
    """Returns Russian translation from English word"""
    if eng_word is None or eng_word == '':
        logger.error('Incorrect arg for `rus_from_eng` func')
        return None

    try:
        data_sample = cur.execute(f"""
                SELECT rus_word
                FROM words
                WHERE eng_word = '{eng_word}';
            """)

        russian_tuple = [i for i in data_sample][0]
        russian_word = russian_tuple[0]
        return russian_word
    except OperationalError as error:
        logger.error(f'OperationalError while getting values from db: {error}')


def eng_from_rus(rus_word=None):
    """Returns English translation from Russian word"""
    if rus_word is None or rus_word == '':
        logger.error('Incorrect arg for `eng_from_rus` func')
        return None

    try:
        data_sample = cur.execute(f"""
                SELECT eng_word
                FROM words
                WHERE rus_word = '{rus_word}';
            """)
        english_tuple = [i for i in data_sample][0]
        english_word = english_tuple[0]
        return english_word
    except OperationalError as error:
        logger.error(f'OperationalError while getting values from db: {error}')


def get_random():
    """Gets a random pair of words"""
    try:
        db_count = db_len()
        for i in range(db_count):
            random_num = randint(1, db_count)
            result = cur.execute(f"""
                SELECT eng_word, rus_word
                FROM words
                WHERE id = '{random_num}';
            """)
            for i in result:
                yield i
    except OperationalError as error:
        logger.error(f'Something went wrong in the main func: {error}')


for i in get_random():
    print(i)

conn.commit()
logger.info('Connection closed successfully...')
cur.close()

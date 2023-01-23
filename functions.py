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
from sqlite3 import OperationalError
from random import choice

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
        (eng_word TEXT NOT NULL UNIQUE,
        rus_word TEXT NOT NULL UNIQUE);
    """)
    logger.info('Connection established successfully...')
except OperationalError as error:
    logger.critical(f'Connection error to database! {error}')
    exit()


def insert_word(eng_word=None, rus_word=None):
    """Adds new word-pair to database"""
    if eng_word is None or rus_word is None:
        logger.error('Incorrect args for `insert_word` func')
        return None

    try:
        cur.execute(f"""
            INSERT INTO words VALUES
            ('{eng_word}', '{rus_word}');
        """)
        logger.info(f'Words {eng_word}:{rus_word} successfully added to db')
    except OperationalError as e:
        logger.error(f'OperationalError while inserting new values to db: {e}')


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


def get_all():
    """Yields a tuple of eng:rus word pairs for all """
    try:
        result = cur.execute("""
                    SELECT *
                    FROM words;
                """)
        for i in result:
            yield choice(result)
    except OperationalError as error:
        logger.error(f'OperationalError while getting values from db: {error}')


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


conn.commit()
logger.info('Connection closed successfully...')
cur.close()

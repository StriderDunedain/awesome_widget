"""
-------->
These functions get response from a database of words using SQLite queries.
-------->
All functions return a tuple like this: ('eng_word', 'rus_word')
By default:
 - The database is called 'database.db'
 - The table is called 'words'
-------->
"""

import sqlite3
from sqlite3 import OperationalError
import logging
from sys import stdout

logging.basicConfig(
    level=logging.DEBUG,
    filename='logs.log',
    format='%(asctime)s [%(levelname)s] |%(lineno)s| > %(message)s',
    filemode='w'
)

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(stream=stdout)
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
        error = 'Incorrect args for `insert_word` func'
        logger.error(error)
        return None

    try:
        cur.execute(f"""
            INSERT INTO words VALUES
            ('{eng_word}', '{rus_word}');
        """)
        logger.info(f'Word-pair {eng_word}:{rus_word} successfully added to database')
    except OperationalError as error:
        logger.error(f'OperationalError while inserting new values to db: {error}')


def get_pair_eng(eng_word=None):
    """Returns a translation of given word (word=ENG)"""
    if eng_word is None or eng_word == '':
        error = 'Incorrect arg for `get_pair_eng` func'
        logger.error(error)
        return None

    try:
        data_sample = cur.execute(f"""
                SELECT eng_word, rus_word
                FROM words
                WHERE eng_word = '{eng_word}';
            """)
        logger.info(f'Selected translation for {eng_word}')

        result_tuple = [i for i in data_sample][0]
        return result_tuple
    except OperationalError as error:
        logger.error(f'OperationalError while getting values from db: {error}')


def get_pair_rus(rus_word=None):
    """Returns a translation of given word (word=RUS)"""
    if rus_word is None or rus_word == '':
        error = 'Incorrect arg for `get_pair_rus` func'
        logger.error(error)
        return None

    try:
        data_sample = cur.execute(f"""
                SELECT eng_word, rus_word
                FROM words
                WHERE rus_word = '{rus_word}';
            """)
        logger.info(f'Selected translation for {rus_word}')

        result_tuple = [i for i in data_sample][0]
        return result_tuple
    except OperationalError as error:
        logger.error(f'OperationalError while getting values from db: {error}')


def get_all():
    """Returns a translation of given word (word=ENG)"""
    try:
        result = cur.execute("""
                    SELECT *
                    FROM words;
                """)
        logger.info('Returned all')
        final = [i for i in result]
        return final
    except OperationalError as error:
        logger.error(f'OperationalError while getting values from db: {error}')


def delete_record(eng_word=None):
    """Deletes a record from database. Arg is ONLY in English!"""
    if eng_word is None:
        error = 'Not expected `eng_word` to equal None'
        logger.error(error)
        return None
    try:
        cur.execute(f"""
            DELETE FROM words WHERE eng_word = '{eng_word}';
        """)
        logger.info('Word-pair successfully deleted from database')
    except OperationalError as error:
        logger.error(f'OperationalError while deleting from database: {error}')


conn.commit()
logger.info('Connection closed successfully...')
cur.close()

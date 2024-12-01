import mysql.connector
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DAL:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                user=os.getenv('DB_USER', 'root'),
                password=os.getenv('DB_PASSWORD', 'default_password'),
                database=os.getenv('DB_DATABASE', 'project10'),
                autocommit=True
            )
            logger.info("Database connection established successfully.")
        except mysql.connector.Error as err:
            logger.error(f"Error connecting to database: {err}")
            self.connection = None

    def _validate_query_params(self, query, params):
        if not isinstance(query, str):
            raise ValueError("Query must be a string.")
        if params is not None and not isinstance(params, tuple):
            raise ValueError("Params must be a tuple or None.")

    def _execute_query(self, query, params=None, fetchall=False, fetchone=False):
        self._validate_query_params(query, params)
        if self.connection:
            try:
                with self.connection.cursor(dictionary=True) as cursor:
                    logger.info(f"Executing query: {query}")
                    if params:
                        logger.info(f"With parameters: {params}")
                    cursor.execute(query, params)
                    if fetchall:
                        result = cursor.fetchall()
                        logger.info(f"Fetched {len(result)} rows")
                        return result
                    elif fetchone:
                        result = cursor.fetchone()
                        logger.info("Fetched one row")
                        return result
                    else:
                        logger.info(f"Query affected {cursor.rowcount} rows")
                    return cursor
            except mysql.connector.Error as err:
                logger.error(f"Error executing query: {err}")
        return None

    def get_table(self, query, params=None):
        return self._execute_query(query, params, fetchall=True)

    def get_scalar(self, query, params=None):
        return self._execute_query(query, params, fetchone=True)

    def insert(self, query, params=None):
        return self._execute_query(query, params)

    def update(self, query, params=None):
        return self._execute_query(query, params)

    def delete(self, query, params=None):
        return self._execute_query(query, params)

    def get_one(self, query, params=None):
        return self._execute_query(query, params, fetchone=True)

    def close(self):
        if self.connection:
            self.connection.close()
            logger.info("Connection closed.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            logger.error(f"An error occurred: {exc_val}")
            logger.exception(f"Exception traceback: {exc_tb}")
        if self.connection:
            self.close()

if __name__ == '__main__':
    with DAL() as dal:
        logger.info("\n=== get_table examples ===")
        countries = dal.get_table("SELECT * FROM countries")
        users = dal.get_table("SELECT * FROM users WHERE age > %s", (25,))

        for country in countries:
            logger.info(f"Country: {country['name']}, Population: {country['population']}")
       
        for user in users:
            logger.info(f"User: {user['name']}, Age: {user['age']}")

        logger.info("\n=== insert examples ===")
        dal.insert(
            "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)",
            ('Johnny1', 'johnny1@example.com', 35)
        )
        dal.insert(
            "INSERT INTO countries (name, code) VALUES (%s, %s)",
            ('Brazil', 'BR')
        )

        logger.info("\n=== update examples ===")
        dal.update(
            "UPDATE users SET age = %s WHERE id = %s",
            (31, 1)
        )

        logger.info("\n=== delete examples ===")
        dal.delete(
            "DELETE FROM users WHERE id = %s",
            (1,)
        )

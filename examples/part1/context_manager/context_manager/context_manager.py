import sqlite3


class db_conn:

    def __init__(self, db_name):
        self.db_name = db_name

    # Открываем подключение к БД
    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    # Закрываем подключение к БД
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.close()
        if exc_value:
            raise


if __name__ == "__main__":
    db = "test_context_connect.db"

    with db_conn(db) as conn:
        cursor = conn.cursor()

import sqlite3
from contextlib import contextmanager


# Схема конструирования следующая: всё, что написано до оператора yield - вызывается в рамках функции __enter__,
# всё что после – в рамках __exit__.
@contextmanager
def db_conn(db_name):
    # Открываем подключение к БД
    conn = sqlite3.connect(db_name)

    yield conn

    # Закрываем подключение к БД
    conn.close()


if __name__ == "__main__":
    db = "test_contextlib_connect.db"

    with db_conn(db) as conn:
        cursor = conn.cursor()

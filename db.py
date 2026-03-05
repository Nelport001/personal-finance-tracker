import sqlite3

DB_NAME = "finance.db"

def get_connection() ->  sqlite3.Connection:
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row 

    return conn

def init_db() -> None:
    with get_connection() as conn:
        conn.execute()
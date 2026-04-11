# sqlite3 DB 연결 객체 반환 유틸리티

import sqlite3
from contextlib import contextmanager

DB_FILENAME = "modakbul.db"

@contextmanager
def get_db_connection():
    """
    DB connection을 생성하고 관리하는 유틸리티입니다.
    사용법 : with get_db_connection() as conn:
    """
    conn = sqlite3.connect(DB_FILENAME)
    conn.row_factory = sqlite3.Row
    try:
        yield
    finally:
        conn.close()
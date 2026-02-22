from psycopg_pool import ConnectionPool

DB_CONN_URL ="postgresql://postgres:admin@localhost:5433/keells"

pool = ConnectionPool(conninfo=DB_CONN_URL, max_size=10)


def get_db_conn():
    return pool.connection()

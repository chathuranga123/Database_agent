from database_connection import get_db_conn


def create_user(name: str, email: str):
    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            # Insert user
            cursor.execute(
                """
                INSERT INTO users (name, email)
                VALUES (%s, %s)
                RETURNING id, name, email
                """,
                (name, email)
            )

            return cursor.fetchone()


def get_user(user_id:int):
    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT id,name,email FROM users where id=%s
                """,(user_id,)
            )
            return  cursor.fetchone()


def get_all_user():
    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT id,name,email FROM users order by id asc 
                """
            )
            return  cursor.fetchall()


def delete_user(user_id:int):
    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM users where id=%s
                """,
                (user_id,)
            )







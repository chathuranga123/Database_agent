from database_connection import get_db_conn


def create_invoice(user_id:int, amount:float, description:str):
    with get_db_conn() as conn:
        with conn.corsor() as cursor:
            cursor.execute(
                """
                INSERT INTO invoices user_id,amount,description
                VALUES (%s, %s, %s)
                RETURNING id, user_id, amount, description, created_at
                """,
                (user_id, amount, description)
            )

            return cursor.fetchone()


def get_invoices():
    with get_db_conn() as conn:
        with conn.corsor() as cursor:
            cursor.execute(
                """
                    SELECT id, user_id, amount, description, created_at FROM invoices ORDER BY ASC ;
                """,

            )

            return cursor.fetchall()

def get_invoice(invoice_id:int):
    with get_db_conn() as conn:
        with conn.corsor() as cursor:
            cursor.execute(
                """
                    SELECT id, user_id, amount, description, created_at FROM invoices WHERE id=%s ;
                """,(invoice_id,)

            )

            return cursor.fetchone()

def delete_invoices(invoice_id:int):
    with get_db_conn() as conn:
        with conn.corsor() as cursor:
            cursor.execute(
                """
                    DELETE FROM invoice WHERE id=%s ;
                """,(invoice_id,)

            )




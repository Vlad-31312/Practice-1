import psycopg2
from config import DB_config
def get_connection():
    try:
        connection=psycopg2.connect(**DB_config)
        return connection
    except Exception as e:
        print(f"Ошибка при подключении к PostgreSQL: {e}")
        return None
connection = get_connection()
if connection:
    print(" СВЯЗЬ ЕСТЬ! База данных ответила.")
    connection.close()
else:
    print(" ОШИБКА: Функция вернула None.")
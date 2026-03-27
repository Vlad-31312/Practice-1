import csv
from connect import get_connection


def import_csv(file_name):
    conn = get_connection()
    if not conn:
        return

    cur=conn.cursor()

    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for row in reader:
                cur.execute(
                    """INSERT INTO contacts (first_name, last_name, phone_number)
                       VALUES (%s, %s, %s)
                       ON CONFLICT (phone_number) DO NOTHING""",
                    (row['first_name'], row['last_name'], row['phone_number'])
                )

        conn.commit()
        print(" CSV импортирован")

    except Exception as e:
        conn.rollback()
        print("Ошибка:", e)

    finally:
        cur.close()
        conn.close()


def add_contact():
    conn = get_connection()
    if not conn:
        return

    cur = conn.cursor()

    try:
        first_name = input("Имя: ")
        last_name = input("Фамилия: ")
        phone = input("Телефон: ")

        cur.execute(
            """INSERT INTO contacts (first_name, last_name, phone_number)
               VALUES (%s, %s, %s)""",
            (first_name, last_name, phone)
        )

        conn.commit()
        print(" Контакт добавлен")

    except Exception as e:
        conn.rollback()
        print(" Ошибка:", e)

    finally:
        cur.close()
        conn.close()

def find_contacts():
    conn = get_connection()
    if not conn:
        return

    cur = conn.cursor()

    try:
        pattern = input("Введите имя или начало номера: ")

        cur.execute(
            """SELECT * FROM contacts
               WHERE first_name ILIKE %s OR phone_number LIKE %s""",
            (f"{pattern}%", f"{pattern}%")
        )

        rows = cur.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("Ничего не найдено")

    except Exception as e:
        print(" Ошибка:", e)

    finally:
        cur.close()
        conn.close()


def update_contact():
    conn = get_connection()
    if not conn:
        return

    cur = conn.cursor()

    try:
        phone = input("Введите телефон контакта для изменения: ")
        new_name = input("Новое имя: ")
        new_last = input("Новая фамилия: ")
        new_phone = input("Новый телефон: ")
        cur.execute(
            """UPDATE contacts
               SET first_name=%s, last_name=%s, phone_number=%s
               WHERE phone_number=%s""",
            (new_name, new_last, new_phone, phone)
        )
        conn.commit()
        print(" Контакт обновлён")

    except Exception as e:
        conn.rollback()
        print(" Ошибка:", e)

    finally:
        cur.close()
        conn.close()


def delete_contact():
    conn = get_connection()
    if not conn:
        return

    cur = conn.cursor()

    try:
        value = input("Введите имя или телефон: ")

        cur.execute(
            """DELETE FROM contacts
               WHERE first_name=%s OR phone_number=%s""",
            (value, value)
        )
        conn.commit()
        print(" Контакт удалён")

    except Exception as e:
        conn.rollback()
        print(" Ошибка:", e)
    finally:
        cur.close()
        conn.close()


def create_table():
    conn = get_connection()
    if not conn:
        return

    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            phone_number VARCHAR(20) PRIMARY KEY
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def main():
    create_table()

    while True:
        print("\n PHONEBOOK MENU")
        print("1. Добавить контакт")
        print("2. Импорт из CSV")
        print("3. Найти контакт")
        print("4. Обновить контакт")
        print("5. Удалить контакт")
        print("0. Выход")

        choice = input("Выбор: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            file_name=input("Введите имя файла CSV:")
            import_csv(file_name)
        elif choice == "3":
            find_contacts()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            print("Выход...")
            break
        else:
            print("Неверный выбор!")
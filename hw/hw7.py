import sqlite3
conn = sqlite3.connect('homework.db')

def create_connection():
    conn = sqlite3.connect('homework.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            quantity INTEGER,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()


def add_product(name, category, quantity, price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (name, category, quantity, price)
        VALUES (?, ?, ?, ?)
    ''', (name, category, quantity, price))
    conn.commit()
    conn.close()
    print(f"Товар '{name}' успешно добавлен.")

def get_all_products():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_product_price(product_id, new_price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    conn.commit()
    conn.close()
    print(f"Цена товара с ID {product_id} обновлена.")

def delete_product(product_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()
    print(f"Товар с ID {product_id} удален.")


if __name__ == "__main__":

    create_table()

    add_product("Ноутбук", "Электроника", 5, 55000.0)
    add_product("Мышь", "Периферия", 20, 1200.5)

    print("\nСписок товаров:")
    for product in get_all_products():
        print(product)

    update_product_price(1, 60000.0)

    delete_product(2)

    print("\nИтоговый список:")
    for product in get_all_products():
        print(product)
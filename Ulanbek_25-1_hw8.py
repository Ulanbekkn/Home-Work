import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table_products(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def select_all_table(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_cheap_product(conn):
    try:
        sql = '''SELECT * FROM products WHERE price < 100 AND quantity > 5'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_search_product(conn, word):
    try:
        sql = '''SELECT * FROM products WHERE full_name LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (f'%{word}%'))
        rows = cursor.fetchall()
        for i in rows:
            print(i)
    except sqlite3.Error as e:
        print(e)

def insert_table(conn, product):
    try:
        sql = '''INSERT INTO products(product_title, price, quantity) VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_quantity(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_price(conn, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(conn, product):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (product,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


sql_table_products = '''
CREATE TABLE products(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) NOT NULL DEFAULT 0.0
)
'''

database = 'hw.db'
connection = create_connection(database)

if connection is not None:
    # create_table_products(connection, sql_table_products)
    # select_all_table(connection)
    # insert_table(connection, ('Iphone 12', 75000.12, 5))
    # insert_table(connection, ('TV Samsung', 24000.56, 10))
    # insert_table(connection, ('Laptop', 34500.34, 7))
    # insert_table(connection, ('Pen', 450000.54, 20))
    # insert_table(connection, ('Window', 98756.00, 20))
    # insert_table(connection, ('Samsung A6', 19000.65, 20))
    # insert_table(connection, ('LG 45', 33800.87, 20))
    # insert_table(connection, ('Bike', 7900.23, 20))
    # insert_table(connection, ('Mac', 156900.54, 20))
    # insert_table(connection, ('Xiami', 458900.34, 20))
    # insert_table(connection, ('Huaway', 23443.45, 20))
    # insert_table(connection, ('Hat', 46865.56, 20))
    # insert_table(connection, ('Ball', 231456.76, 20))
    # insert_table(connection, ('Canon mf3010', 5465423.21, 20))
    # insert_table(connection, ('Apple watch', 97.34, 10))
    # update_quantity(connection, (25, 1))
    # update_price(connection, (55000.34, 1))
    # delete_product(connection, 1)
    # select_cheap_product(connection)
    print('Done')
    connection.close()

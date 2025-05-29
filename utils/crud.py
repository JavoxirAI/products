from core.database_settings import execute_query


def add_product():
    name = input("Product name: ")
    quantity = input("Product name: ")

    params = (name, quantity,)
    query = "INSERT INTO products (name, quantity) VALUES (%s, %s)"
    execute_query(query=query, params=params)

    print("New product is added.")


def show_products():
    query = "SELECT * FROM products;"
    products = execute_query(query=query, fetch="all")
    for product in products:
        print(dict(product))


def delete_product():
    product_id = input("Product id: ")
    params = (product_id,)
    query = "DELETE FROM products WHERE id = %s;"
    execute_query(query=query, params=params)

    print("Product is deleted")
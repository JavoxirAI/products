import psycopg2
from psycopg2.extras import DictCursor

db_config = {
    "database" : "products",
    "user" : "products",
    "host" : "localhost",
    "port" : "5432",
    "password" : "products-password"
}

conn = psycopg2.connect(**db_config)
cursor = conn.cursor(cursor_factory=DictCursor)

cursor.execute(
    query="""
    CREATE TABLE test(
    id SERIAL PRIMARY KEY,
    test INTEGER DEFAULT 0
    );
    """
)

conn.commit()


print(cursor.fetchall())
print("Done")
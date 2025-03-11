import psycopg2

try:
    conn = psycopg2.connect(
        dbname="test_docker",
        user="arun",
        password="root",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    # Create a table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            age INT
        );
    """)

    # Insert data
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Alice", 25))

    # Fetch data
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    for user in users:
        print(user)

    conn.commit()  # Save changes
    cursor.close()
    conn.close()

except Exception as error:
    print("Error:", error)


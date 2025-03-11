from flask import Flask 

import psycopg2


app = Flask(__name__)


def saveUser():
    try:
        print("save user")
        conn = psycopg2.connect(
            dbname="test_docker",
            user="arun",
            password="root",
            host="postgres_db",
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

        print("inserting data ")
        # Insert data
        cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Alice", 25))

        print("data inserted")
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



@app.route("/")
def home():
    return "hhhhh"

@app.route('/save_user')
def hello_world():
    saveUser()
    return "save user to database"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)



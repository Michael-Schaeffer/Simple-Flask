import mysql.connector

class User:
    @classmethod
    def connect(cls):
        try:
            conn = mysql.connector.connect(   
                host="localhost",
                database="users",
                user="root",
                password="xxxx"
            )
            return conn
        except mysql.connector.Error as err:
            print("Database connection error:", err)
            return "Database connection failed"

    @classmethod
    def create_table(cls):
        conn = cls.connect()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS user (
                    user_id INTEGER PRIMARY KEY AUTO_INCREMENT,
                    first_name VARCHAR(50) NOT NULL,
                    last_name VARCHAR(50) NOT NULL
                )
            """)
            return "Table created"
        except Exception as err:
            print(f"Error creating table: {err}")
            return "Table creation failed"

    @classmethod
    def add_user_data(cls):
        conn = cls.connect()
        try:
            cursor = conn.cursor()
            query = "INSERT INTO user (first_name, last_name) VALUES (%s, %s)"
            data = [
                ("John", "Doe"),
                ("Michael", "Schaeffer")
                ]
            for user in data:
                cursor.execute(query, user)
            conn.commit()
            conn.close()
            return "User data added"
        except Exception as err:
            print(f"Error add user data: {err}")
            return "Add user data failed"

    @classmethod
    def delete_user_data(cls, user_id):
        conn = cls.connect()
        try:
            cursor = conn.cursor()
            query = "DELETE FROM user WHERE user_id = %s"
            data = (str(user_id),)
            cursor.execute(query, data)
            conn.commit()
            conn.close()
            return "User data deleted"
        except Exception as err:
            print(f"Error delete user data: {err}")
            return "Delete user data failed"

    @classmethod
    def fetch_all_user_data(cls):
        conn = cls.connect()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user")
            return cursor.fetchall()
        except Exception as err:
            print(f"Error fetch user data: {err}")
            return "Fetch user data failed"

    @classmethod
    def show_databases(cls):
        conn = cls.connect()
        try:
            cursor = conn.cursor()
            cursor.execute("SHOW DATABASES")
            databases = list()
            for db in cursor:
                databases.append(db)
            return databases
        except Exception as err:
            print(f"Error show databases: {err}")
            return "Show databases failed"
# Task 1
from mysql_connect import connect_database

conn = connect_database()
if conn is not None:
    def add_members(name, age):
        try:
            cursor = conn.cursor()

            new_member = ('Kevin Smith', 19)

            query_check = 'SELECT * FROM members WHERE name = Kevin%'
            if query_check:
                print("Running query...")
                print("\nMember already exists.")
                return conn
            else:
                query = 'INSERT INTO members (name, age) VALUES(%s, %s)'

                cursor.execute(query, new_member)
                conn.commit()
                print("\nNew customer added successfully.")

        finally:
            cursor.close()
            conn.close()
            
else:
    print("\nConnection to database was unsuccessful.")

add_members('name', 'age')
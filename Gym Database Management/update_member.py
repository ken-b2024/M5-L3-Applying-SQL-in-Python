# Task 3
from mysql_connect import connect_database

conn = connect_database()
if conn is not None:
    def update_members(id, new_age):
        try:
            cursor = conn.cursor()

            id = 6
            new_age = 22

            query_check = 'SELECT COUNT(*) AS total FROM members WHERE id = 6'
            cursor.execute(query_check)
            result = cursor.fetchone()
            if result[0] == 0:
                print("Running query...")
                print("\nMember with this id does not exist.")
                return conn
            else:
                query = 'UPDATE members SET age = 22 WHERE id = 6'
                cursor.execute(query)
                conn.commit()
                print("\nCustomer successfully updated.")

        finally:
            cursor.close()
            conn.close()
            
else:
    print("\nConnection to database was unsuccessful.")

update_members('id', 'new_age')
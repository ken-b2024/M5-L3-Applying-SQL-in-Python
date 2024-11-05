# Task 1
from mysql_connect import connect_database

conn = connect_database()
if conn is not None:
    def get_members_in_age_range(start_age,end_age):
        try:
            cursor = conn.cursor()

            start_age = 25
            end_age = 30

            query = 'SELECT * FROM members WHERE age BETWEEN 25 AND 30'

            cursor.execute(query)
            for row in cursor.fetchall():
                print("\nFetching data...\n")
                print(row)

        finally:
            cursor.close()
            conn.close()
            
else:
    print("\nConnection to database was unsuccessful.")

get_members_in_age_range('start_age','end_age')
# Task 4
from mysql_connect import connect_database

conn = connect_database()
if conn is not None:
    def delete_members(member_id):
        try:
            cursor = conn.cursor()

            member_id = 3

            query_check = 'SELECT COUNT(*) AS total FROM workoutsessions WHERE member_id = 3'
            cursor.execute(query_check)
            result = cursor.fetchone()
            if result[0] == 0:
                print("Running query...")
                print("\nMember ID is invalid.")
                return conn
            else:
                query = 'DELETE FROM workoutsessions WHERE member_id = 3'
                cursor.execute(query)
                conn.commit()
                print("\nWorkout session was successfully removed from database.")

        finally:
            cursor.close()
            conn.close()
            
else:
    print("\nConnection to database was unsuccessful.")

delete_members('member_id')
# Task 2
from mysql_connect import connect_database

conn = connect_database()
if conn is not None:
    def add_workout(member_id, session_date, session_time, activity):
        try:
            cursor = conn.cursor()

            new_workout = (6, '2024-08-02', '11:00-12:00 PM', 'Back, Biceps, Triceps, Core strength')

            query_check = 'SELECT COUNT(*) AS total FROM workoutsessions WHERE member_id = 6 AND session_date = 2024-05-02'
            cursor.execute(query_check)
            result = cursor.fetchone()

            if result[0] != 0:
                user_action = input("\nUser with this ID already has a session scheduled for this date. Do you still want to add this entry? (y/n): ")
                if user_action == 'y':
                    query = 'INSERT INTO workoutsessions (member_id, session_date, session_time, activity) VALUES(%s, %s, %s, %s)'
                    cursor.execute(query, new_workout)
                    conn.commit()
                    print("\nNew workout has been added successfully.")

                else:
                    print("\nReturning to database.")
            else:
                query = 'INSERT INTO workoutsessions (member_id, session_date, session_time, activity) VALUES(%s, %s, %s, %s)'

                cursor.execute(query, new_workout)
                conn.commit()
                print("\nNew workout has been added successfully.")

        finally:
            cursor.close()
            conn.close()

add_workout('member_id', 'session_date', 'session_time', 'activity')
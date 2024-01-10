import sqlite3

def create_projects_table():
    try:
        conn = sqlite3.connect('project.db')
        cursor = conn.cursor()

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS projects (
                project_id INTEGER PRIMARY KEY,
                project_name TEXT NOT NULL,
                start_date TEXT NOT NULL
            );
        '''

        cursor.execute(create_table_query)
        conn.commit()

        print("Table 'projects' created successfully.")

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        conn.close()

def insert_projects_data():
    try:
        conn = sqlite3.connect('project.db')
        cursor = conn.cursor()
        projects_data = [
            ('Project 1', '2022-01-01'),
            ('Project 2', '2022-02-15'),
            ('Project 3', '2022-03-20'),
        ]

        insert_data_query = '''
            INSERT INTO projects (project_name, start_date)
            VALUES (?, ?);
        '''
        for project in projects_data:
            cursor.execute(insert_data_query, project)

        conn.commit()
        print("Data inserted into 'projects' table successfully.")

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        conn.close()

if __name__ == "__main__":
    create_projects_table()
    insert_projects_data()

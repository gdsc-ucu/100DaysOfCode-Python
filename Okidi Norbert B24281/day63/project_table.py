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

def fetch_projects():
    try:
        conn = sqlite3.connect('project.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM projects")
        projects = cursor.fetchall()

        print("All Projects")
        for project in projects:
            print(project)
        
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def insert_multiple_projects(projects_data):
    try:
        conn = sqlite3.connect('project.db')
        cursor = conn.cursor()
        cursor.execute('BEGIN TRANSACTION')

        try:
            insert_data_query = '''
                INSERT INTO projects (project_name, start_date)
                VALUES (?, ?);
            '''
            for project in projects_data:
                cursor.execute(insert_data_query, project)

            conn.commit()
            print("Data inserted into 'projects' table successfully.")
        except sqlite3.Error as e:
             conn.rollback()
             print(f"Error during transaction: {e}")

    except sqlite3.Error as e:
            print(f"Error: {e}")

    finally:
            conn.close()

if __name__ == "__main__":
    create_projects_table()


    multiple_projects_data = [
         ('project 4', '2023-05-01'),
         ('project 5', '2023-06-01'),
         ('project 6', '2023-07-01'),
         ('project 7', '2023-08-01'),
         ('project 8', '2023-09-01'),
         ('project 9', '2023-10-01'),
    ]
    insert_multiple_projects(multiple_projects_data)
    fetch_projects()

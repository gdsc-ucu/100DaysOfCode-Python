import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('projects.db')
        print("Database created successfully")
    except sqlite3.Error as e:
        print(e)

def create_table():
    conn = sqlite3.connect('projects.db')
    cursor = conn.cursor()
    sql_query = '''
        CREATE TABLE projects (
            project_id INTERGER PRIMARY KEY,
            project_name TEXT NOT NULL,
            start_date TEXT NOT NULL
        );
    '''

    print("Table 'project' created successfully")

    cursor.execute(sql_query)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    create_table()
import sqlite3

def create_multiple_tables():
    try:
        conn = sqlite3.connect('project.db')

        cursor = conn.cursor()
        create_employees_table_query = '''
            CREATE TABLE IF NOT EXISTS employees (
                employee_id INTEGER PRIMARY KEY,
                employee_name TEXT NOT NULL
            );
        '''


        create_projects_table_query = '''
            CREATE TABLE IF NOT EXISTS projects (
                project_id INTEGER PRIMARY KEY,
                project_name TEXT NOT NULL,
                start_date TEXT NOT NULL
            );
        '''


        create_assignments_table_query = '''
            CREATE TABLE IF NOT EXISTS assignments (
                assignment_id INTEGER PRIMARY KEY,
                employee_id INTEGER,
                project_id INTEGER,
                FOREIGN KEY (employee_id) REFERENCES employees (employee_id),
                FOREIGN KEY (project_id) REFERENCES projects (project_id)
            );
        '''


        cursor.execute(create_employees_table_query)
        cursor.execute(create_projects_table_query)
        cursor.execute(create_assignments_table_query)

        conn.commit()

        print("Tables created successfully.")

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        conn.close()

def insert_sample_data():
    try:
        conn = sqlite3.connect('project.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO employees (employee_name) VALUES ('Employee 1')")
        cursor.execute("INSERT INTO employees (employee_name) VALUES ('Employee 2')")
        cursor.execute("INSERT INTO employees (employee_name) VALUES ('Employee 3')")


        cursor.execute("INSERT INTO projects (project_name, start_date) VALUES ('Project 1', '2022-01-01')")
        cursor.execute("INSERT INTO projects (project_name, start_date) VALUES ('Project 2', '2022-02-15')")
        cursor.execute("INSERT INTO projects (project_name, start_date) VALUES ('Project 3', '2022-03-20')")

        cursor.execute("INSERT INTO assignments (employee_id, project_id) VALUES (1, 1)")
        cursor.execute("INSERT INTO assignments (employee_id, project_id) VALUES (2, 2)")

        conn.commit()

        print("Sample data inserted successfully.")

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        conn.close()

def fetch_unassigned_employees():
    try:
        conn = sqlite3.connect('project.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT e.employee_id, e.employee_name
            FROM employees e
            LEFT JOIN assignments a ON e.employee_id = a.employee_id
            WHERE a.project_id IS NULL
        ''')

        unassigned_employees = cursor.fetchall()

        print("Unassigned Employees:")
        for employee in unassigned_employees:
            print(employee)

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        conn.close()

if __name__ == "__main__":
    create_multiple_tables()
    insert_sample_data()

    fetch_unassigned_employees()

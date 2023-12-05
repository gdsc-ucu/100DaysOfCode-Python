import sqlite3

def create_tables():
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

def insert_employee_data(employee_name):
    try:
        conn = sqlite3.connect('project.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO employees (employee_name) VALUES (?)", (employee_name,))

        conn.commit()

        print(f"Employee '{employee_name}' inserted successfully.")

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        conn.close()

def fetch_all_employees():
    try:
        conn = sqlite3.connect('project.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM employees;            
        ''')

        employees = cursor.fetchall()

        print("All Employees:")
        for employee in employees:
            print(employee)

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        conn.close()

def main():
    create_tables()
    while True:
        print("\nSelect Options:")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Exit")

        input_option = input("Enter your Option [1,2 or 3]: ")

        if input_option == '1':
            employee_name = input("Enter the employee's name: ")
            insert_employee_data(employee_name)

        elif input_option == '2':
            fetch_all_employees()

        elif input_option == '3':
            print("Exiting the program")
            break

        else:
            print("Invalid option: please enter a rang of 1-3 only.")


if __name__ == "__main__":
    main()
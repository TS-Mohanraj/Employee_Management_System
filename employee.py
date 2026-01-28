from database import get_connection

def add_employee():
    name = input("Enter name:")
    email = input("Enter email:")
    phone = input("Enter phone:")
    address = input("Enter address:")
    post = input("Enter post:")
    salary = float(input("Enter salary:"))

    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO employees(name,email,phone,address,post,salary) VALUES(%s,%s,%s,%s,%s,%s)"
    values = (name,email,phone,address,post,salary)
    cursor.execute(query,values)
    conn.commit()

    print(f"Employee added successfully! Employee ID:{cursor.lastrowid}")
    cursor.close()
    conn.close()

def search_employee():
    emp_id = int(input("Enter Employee ID:"))

    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM employees WHERE emp_id = %s"
    val = (emp_id)
    cursor.execute(query,val)
    result = cursor.fetchone()

    if result:
        print(f"----------------------")
        print(f"Employee Details")
        print(f"----------------------")
        print("ID:",result[0])
        print("Name:",result[1])
        print("Email:",result[2])
        print("Phone:",result[3])
        print("Address:",result[4])
        print("Post:",result[5])
        print("Salary:",result[6])
    else:
        print("Employee id not exists!")
    cursor.close()
    conn.close()

def view_employee():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    allresult = cursor.fetchall()

    if not allresult:
        print("No records found!")
    else:
        print("------Employee Records-------")
        for emp in allresult:
            print(emp)
    cursor.close()
    conn.close()

def update_employee():
    emp_id = int(input("Enter Employee ID to update:"))
    email = input("Enter new email:")
    phone = input("Enter new phone:")
    address = input("Enter new address:")

    conn = get_connection()
    cursor = conn.cursor()

    query = "UPDATE employees SET email=%s,phone=%s,address=%s WHERE emp_id=%s"
    val = (email,phone,address,emp_id)
    cursor.execute(query,val)

    if cursor.rowcount == 0:
        print("Employee not found.")
    else:
        print("Employee details update successfully!")
    conn.commit()
    cursor.close()
    conn.close()

def promote_employee():
    emp_id = input("Enter the employee ID to promote:")
    post1 = input("Enter the newly promoted post:")
    increment = float(input("Enter the salary increment amount:"))

    conn = get_connection()
    cursor = conn.cursor()

    query = "UPDATE employees SET post=%s,salary = salary + %s WHERE emp_id=%s"
    val = (post1,increment,emp_id)
    cursor.execute(query,val)
    conn.commit()

    if cursor.rowcount == 0:
        print("Employee not found.")
    else:
        print("Employee promoted successfully!")
    cursor.close()
    conn.close()

def delete_employee():
    emp_id = input("Enter the Employee ID to delete:")

    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM employees WHERE emp_id=%s"
    val = (emp_id)
    cursor.execute(query,val)
    conn.commit()

    if cursor.rowcount ==0:
        print("Employee not found")
    else:
        print("Employee deleted successfully!")
    
    cursor.close()
    conn.close()


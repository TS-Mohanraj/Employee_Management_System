import pymysql

def get_connection():
    return pymysql.connect(host="localhost",user="root",password="password",database="myemployees")

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS employees(emp_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100),email VARCHAR(30),phone VARCHAR(20), address VARCHAR(200),post VARCHAR(30),salary FLOAT)""")
    conn.commit()

    cursor.close()
    conn.close()


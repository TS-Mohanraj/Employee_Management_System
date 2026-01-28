 # 🧑‍💼 Employee Management System (Python + MySQL)

 ## 📌 Project Overview
This is a console-based Employee Management System developed using Python and MySQL. ...

## ✨ Features
- Add new employee records  
- Auto-generated employee ID  
- Search employee details  
...

 ## 🛠️ Tech Stack
- Python  
- MySQL  
- PyMySQL

 ## 📂 Project Structure
Employee_Management_System/
├── main.py
├── database.py
├── employee.py
├── README.md
└── requirements.txt

 ## 🗄️ Database Schema
CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address VARCHAR(200),
    post VARCHAR(50),
    salary FLOAT
);

 ## 🚀 How to Run the Project
1. Clone repo  
2. Install dependencies  
3. Create database  
4. Update credentials  
5. Run main.py

 ## 📖 What I Learned
- Connecting Python applications to MySQL  
- Writing SQL queries  
- Handling commit() transactions  
...

 ## 🔮 Future Enhancements
- Update employee details  
- Admin login  
- Input validation  
- GUI interface

## 👤 Author
Mohanraj T S
Aspiring Python and SQL Developer
=======

>>>>>>> 6a41a160afab575550b4bb9ec6ff308bc2b1ebb5

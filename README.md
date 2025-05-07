# Student Management System

This is a simple web-based student management system built with Python, Flask, and MySQL. It allows you to create, read, update, and delete (CRUD) student records, with a tech-inspired blue theme for the design.

## Features
- Add new students with name, age, and major.
- View a list of all students.
- Edit existing student records.
- Delete students from the database.
- Styled with a modern blue theme representing technology.

## Requirements
- Python 3.13.2
- Flask (`pip install flask`)
- MySQL Connector (`pip install mysql-connector-python`)
- MySQL (e.g., via XAMPP with phpMyAdmin)

## Setup Instructions
1. Clone this repository: git clone https://github.com/haadygordon/student-management-system.git
2. Set up a MySQL database named `student_db` and create a `students` table:
```sql
    CREATE TABLE students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        major VARCHAR(100)
    );
```
3. Install the required Python packages: pip install flask mysql-connector-python
4. Run the application: python app.py
5. Open your browser and go to http://127.0.0.1:5000/

## Project Structure
- app.py: The main Flask application.
- templates/: HTML templates for the web pages.
- static/: CSS styles for the blue tech theme.

## Future Improvements
- Add search functionality.
- Include user authentication.
- Enhance the design with more interactive elements.
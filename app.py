from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='student_db'
    )
    return connection

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        major = request.form['major']
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO students (name, age, major) VALUES (%s, %s, %s)', (name, age, major))
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('index'))
    return render_template('add_student.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_student(id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        major = request.form['major']
        cursor.execute('UPDATE students SET name=%s, age=%s, major=%s WHERE id=%s', (name, age, major, id))
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('index'))
    cursor.execute('SELECT * FROM students WHERE id=%s', (id,))
    student = cursor.fetchone()
    cursor.close()
    connection.close()
    return render_template('update_student.html', student=student)

@app.route('/delete/<int:id>')
def delete_student(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM students WHERE id=%s', (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
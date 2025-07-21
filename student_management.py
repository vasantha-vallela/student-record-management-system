import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vasu@123",  # ❗Replace with your actual MySQL password
    database="student_db"
)

cursor = db.cursor()

def menu():
    while True:
        print("\n----- Student Management System -----")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

def add_student():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    branch = input("Enter Branch: ")
    marks = float(input("Enter Marks: "))
    cursor.execute("INSERT INTO students VALUES (%s, %s, %s, %s, %s)", (id, name, age, branch, marks))
    db.commit()
    print("✅ Student added!")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def search_student():
    sid = int(input("Enter ID to search: "))
    cursor.execute("SELECT * FROM students WHERE id=%s", (sid,))
    row = cursor.fetchone()
    if row:
        print(row)
    else:
        print("Student not found.")

def update_student():
    sid = int(input("Enter ID to update: "))
    name = input("New Name: ")
    age = int(input("New Age: "))
    branch = input("New Branch: ")
    marks = float(input("New Marks: "))
    cursor.execute("UPDATE students SET name=%s, age=%s, branch=%s, marks=%s WHERE id=%s",
                   (name, age, branch, marks, sid))
    db.commit()
    print("✅ Student updated!")

def delete_student():
    sid = int(input("Enter ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id=%s", (sid,))
    db.commit()
    print("✅ Student deleted!")

# Run the menu
menu()

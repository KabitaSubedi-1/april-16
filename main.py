import json
import os

DATA_FILE = "students.json"


def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)


def add_student(students):
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")

    students.append({
        "name": name,
        "age": age,
        "grade": grade
    })

    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No students found.")
        return

    print("\n--- Student List ---")
    for i, s in enumerate(students, start=1):
        print(f"{i}. {s['name']} | Age: {s['age']} | Grade: {s['grade']}")


def main():
    students = load_students()

    while True:
        print("\n=== Student Manager ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)
            save_students(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            save_students(students)
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
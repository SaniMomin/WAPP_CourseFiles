def display_menu():
    print("\n--- STUDENT RECORD MANAGER ---")
    print("1. Add student record")
    print("2. View all records")
    print("3. Find student by name")
    print("4. Exit")

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def add_student(records):
    name = input("Enter student name: ").strip()
    try:
        score = float(input("Enter exam score (0-100): "))
        if 0 <= score <= 100:
            grade = calculate_grade(score)
            student = (name, score, grade)
            records.append(student)
            print(f"Record added for {name}.")
        else:
            print("Score must be between 0 and 100.")
    except ValueError:
        print("Invalid score. Please enter a number.")

def view_records(records):
    if not records:
        print("No student records found.")
    else:
        print("\nStudent Records:")
        for idx, (name, score, grade) in enumerate(records, 1):
            print(f"{idx}. Name: {name}, Score: {score}, Grade: {grade}")

def find_student(records):
    name = input("Enter the student name to search: ").strip()
    found = False
    for student in records:
        if student[0].lower() == name.lower():
            print(f"Found: Name: {student[0]}, Score: {student[1]}, Grade: {student[2]}")
            found = True
            break
    if not found:
        print("Student not found.")

def main():
    student_records = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            add_student(student_records)
        elif choice == "2":
            view_records(student_records)
        elif choice == "3":
            find_student(student_records)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

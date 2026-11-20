def add_student():
    roll = input("Enter the student's roll number: ")
    name = input("Enter the student's name: ")
    marks = input("Enter the student's marks: ")
    with open("students.txt", "a") as file:
        file.write(f"{roll},{name},{marks}\n")
        print("Student added successfully.")
def display_students():
    try: 
        with open("students.txt", "r") as file:
            print("\nStudent Records:")
            for line in file:
                roll, name, marks = line.strip().split(",")
                print(f"Roll: {roll}, Name: {name}, Marks: {marks}")
                print("--------------")
    except FileNotFoundError:
        print("No student records found.")
while True:
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
          add_student()
        elif choice == "2":
          display_students()
        elif choice == "3":
          print("Exiting the program.")
          break
        else:
          print("Invalid choice. Please try again.") 
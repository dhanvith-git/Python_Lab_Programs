students = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    status = input("Enter attendance (Present/Absent): ")
    students[name] = status
print("\nAttendance Report:")
for name, status in students.items():
    print(name, ":", status)
present = 0
absent = 0
for status in students.values():
    if status == "Present":
        present += 1
    else:
        absent += 1
print("Total Present:", present)
print("Total Absent:", absent)

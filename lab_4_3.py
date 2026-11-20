import csv

try:
    # Enter number of employees
    n = int(input("Enter number of employees: "))

    # Open CSV file in write mode
    with open("payroll.csv", "w", newline="") as file:

        writer = csv.writer(file)

        # Write column headings
        writer.writerow([
            "ID",
            "Name",
            "Basic Salary",
            "Allowance",
            "Deduction",
            "Net Salary"
        ])

        # Enter employee details
        for i in range(n):

            print("\nEnter Employee Details")

            emp_id = input("Employee ID: ")
            name = input("Employee Name: ")
            basic = float(input("Basic Salary: "))
            allowance = float(input("Allowance: "))
            deduction = float(input("Deduction: "))

            # Calculate Net Salary
            net_salary = basic + allowance - deduction

            # Store employee details in CSV
            writer.writerow([
                emp_id,
                name,
                basic,
                allowance,
                deduction,
                net_salary
            ])

    print("\nPayroll records saved successfully.")

    # Read and display CSV file
    print("\n===== Employee Payroll Records =====")

    with open("payroll.csv", "r") as file:

        reader = csv.reader(file)

        for row in reader:
            print(row)

except ValueError:
    print("Please enter valid numeric values.")
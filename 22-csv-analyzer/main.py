import csv


def analyze_csv(filename):
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        employees = list(reader)

    salaries = [float(employee["Salary"]) for employee in employees]

    total_employees = len(employees)
    average_salary = sum(salaries) / total_employees
    highest_salary = max(salaries)
    lowest_salary = min(salaries)

    highest_paid = max(employees, key=lambda employee: float(employee["Salary"]))

    return (
        total_employees,
        average_salary,
        highest_salary,
        lowest_salary,
        highest_paid
    )


print("===== CSV Analyzer =====")

filename = "sample.csv"

(
    total_employees,
    average_salary,
    highest_salary,
    lowest_salary,
    highest_paid
) = analyze_csv(filename)

print("\nCSV Summary")
print("-----------")

print("Total Employees:", total_employees)
print(f"Average Salary: ${average_salary:,.2f}")
print(f"Highest Salary: ${highest_salary:,.2f}")
print(f"Lowest Salary: ${lowest_salary:,.2f}")

print("\nHighest Paid Employee")
print("---------------------")
print("Name:", highest_paid["Name"])
print("Department:", highest_paid["Department"])
print("Salary:", f"${float(highest_paid['Salary']):,.2f}")
print("Experience:", highest_paid["Experience"], "years")

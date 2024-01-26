######## EXERCISE 1 ########

employee_name = input("Enter employee name: ")
hours_worked = float(input("Enter hours worked: "))
regular_hours = 40 * 22
overtime_hours = 0
total_pay = regular_hours + overtime_hours

if hours_worked > 40:
    hours_worked = hours_worked - 40
    overtime_hours = hours_worked * 1.5
    total_pay = regular_hours + overtime_hours
    print(f"""
Mr/Mrs. {employee_name} over the week you have earned
Regular pay = {regular_hours}
Overtime pay = {overtime_hours}
Total pay = {total_pay}
""")
else:
    print(f"""
Mr/Mrs. {employee_name} over the week you have earned
Regular pay = {regular_hours}
Overtime pay = {overtime_hours}
Total pay = {total_pay}
""")
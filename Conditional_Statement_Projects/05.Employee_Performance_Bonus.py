'''
Employee Performance Bonus Calculator
'''

# Get employee details
employee_name = input("Enter Employee Name: ")
monthly_salary = float(input("Enter Monthly Salary: ₹"))
years_experience = int(input("Enter Years of Experience: "))
rating = int(input("Enter Performance Rating (1-5): "))

# Initialize variables
bonus_percentage = 0
bonus_amount = 0
message = "Keep improving your performance!"

# Validate performance rating
if rating < 1 or rating > 5:
    print("Invalid Performance Rating! Enter a rating between 1 and 5.")

else:
    # Calculate bonus percentage
    if years_experience >= 10 and rating >= 4:
        bonus_percentage = 20

    elif years_experience >= 5 and rating >= 4:
        bonus_percentage = 15

    elif years_experience >= 2 and rating >= 3:
        bonus_percentage = 10

    else:
        bonus_percentage = 0

    # Calculate bonus amount and final salary
    bonus_amount = monthly_salary * bonus_percentage / 100
    final_salary = monthly_salary + bonus_amount

    # Check performance message
    if rating == 5:
        message = "Excellent Performer"

    # Display employee details
    print("\n===== Employee Performance Bonus =====")
    print("Employee Name:", employee_name)
    print("Monthly Salary: ₹", monthly_salary)
    print("Years of Experience:", years_experience)
    print("Performance Rating:", rating)
    print("Bonus Percentage:", bonus_percentage, "%")
    print("Bonus Amount: ₹", bonus_amount)
    print("Final Salary: ₹", final_salary)
    print("Performance Message:", message)

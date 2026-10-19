'''
Student Scholarship Eligibility Checker
'''

# Get user input for student details
student_name = input("Enter Student Name: ")
percentage = float(input("Enter Student Percentage: "))
annual_family_income = float(input("Enter Annual Family Income: "))
attendance = float(input("Enter Attendance Percentage: "))

# Initialize variables
eligibility_status = "Not Eligible"
scholarship_category = "No Scholarship"
reason = "None"

# Check scholarship eligibility
if percentage >= 75 and attendance >= 75 and annual_family_income <= 400000:

    if percentage >= 90:
        eligibility_status = "Eligible for Full Scholarship"
        scholarship_category = "Full Scholarship"

    else:
        eligibility_status = "Eligible for Partial Scholarship"
        scholarship_category = "Partial Scholarship"

else:
    eligibility_status = "Not Eligible"

    # Identify the reason for ineligibility
    if percentage < 75:
        reason = "Percentage below 75%"
    elif annual_family_income > 400000:
        reason = "Annual family income exceeds Rs. 4,00,000"
    elif attendance < 75:
        reason = "Attendance below 75%"

# Display information
print("\n===== Student Scholarship Eligibility =====")
print("Student Name:", student_name)
print("Eligibility Status:", eligibility_status)
print("Scholarship Category:", scholarship_category)
print("Reason for Ineligibility:", reason)






'''
Simple ATM Withdrawal System
'''

# Input from user
name = input("Account Holder Name: ")
current_balance = float(input("Current Balance: "))
withdrawal_amount = float(input("Enter Withdrawal Amount: "))

# Initial transaction status
transaction_status = "Failed"

# Validate withdrawal amount
if withdrawal_amount <= 0:
    print("Invalid Withdrawal Amount")

elif withdrawal_amount > 20000:
    print("Withdrawal Amount Exceeds Transaction Limit of ₹20,000")

elif withdrawal_amount > current_balance:
    print("Insufficient Balance")

else:
    # Process valid withdrawal
    current_balance = current_balance - withdrawal_amount
    transaction_status = "Successful"

    print("Withdrawal Successful")

    if current_balance < 1000:
        print("Warning: Your Current Balance is below ₹1,000")
    else:
        print("Your Current Balance is:", current_balance)

# Display information
print("\n===== SIMPLE ATM WITHDRAWAL SYSTEM =====")
print("Account Holder Name:", name)
print("Transaction Status:", transaction_status)
print("Withdrawal Amount: ₹", withdrawal_amount)
print("Remaining Balance: ₹", current_balance)



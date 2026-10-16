
'''
Online Shopping Checkout
'''

# Getting user input
customer_name = input("Enter your name: ")
purchase_amount = float(input("Enter the purchase amount: "))
customer_type = input("Enter customer type (regular/premium): ").lower()

delivery_charge = 100

# Validate purchase amount
if purchase_amount <= 0:
    print("Invalid purchase amount.")

else:
    # Calculate discount based on purchase amount
    if purchase_amount >= 5000:
        discount_amount = purchase_amount * 20 / 100

    elif purchase_amount >= 3000:
        discount_amount = purchase_amount * 10 / 100

    elif purchase_amount >= 1000:
        discount_amount = purchase_amount * 5 / 100

    else:
        discount_amount = 0

    # Validate customer type and calculate total discount
    if customer_type == "premium":
        premium_discount = purchase_amount * 5 / 100
        total_discount = discount_amount + premium_discount

    elif customer_type == "regular":
        total_discount = discount_amount

    else:
        print("Invalid customer type.")
        exit()

    # Calculate amount after discounts
    discounted_amount = purchase_amount - total_discount

    # Calculate delivery charge
    if discounted_amount >= 2000:
        delivery_charge = 0

    # Calculate final bill
    final_bill = discounted_amount + delivery_charge

    # Display online shopping bill
    print("\n===== ONLINE SHOPPING BILL =====")
    print("Customer Name:", customer_name)
    print("Purchase Amount: ₹", purchase_amount)
    print("Discount Amount: ₹", total_discount)
    print("Delivery Charge: ₹", delivery_charge)
    print("Final Bill: ₹", final_bill)




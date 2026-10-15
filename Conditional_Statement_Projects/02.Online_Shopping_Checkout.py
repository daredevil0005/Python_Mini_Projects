'''
Online Shopping Checkout
'''
#getting user input
customer_name = input("Enter your name: ")
purchase_amount = float(input("Enter the purchase amount:"))
customer_type = input("Enter customer type (regular/premium): ").lower()
delivery_charge=100


#calculating discount based on purchase amount and customer type
if purchase_amount < 0:
    print("Invalid purchase amount. Please enter a positive value.")

else:
    if purchase_amount >= 5000:
        discount_amount = purchase_amount * 20/100

    elif purchase_amount >= 3000 and purchase_amount < 5000:
        discount_amount = purchase_amount * 10/100

    elif purchase_amount >= 1000 and purchase_amount < 3000:
        discount_amount = purchase_amount * 5/100 

    elif purchase_amount < 1000:
        discount_amount = 0


#checking customer type 
if customer_type == "premium":
    final_discount_P = purchase_amount * 5/100 + discount_amount

else:
    final_discount_R = purchase_amount - discount_amount

#calculating final bill
if customer_type == "premium":
    
    if purchase_amount > 2000:

        final_bill_P = purchase_amount - final_discount_P

    else:

        final_bill_P = purchase_amount + delivery_charge - final_discount_P

else:
        if purchase_amount > 2000:

            final_bill_R =  final_discount_R
            
        else:
            
            final_bill_R = final_discount_R + delivery_charge


# Display Online Shopping bill
print("\n===== ELECTRICITY BILL =====")
print("Customer Name:", customer_name)

if customer_type == "premium":
    print("Discount Amount:",final_discount_P)
else:
    print("Discount Amount:",discount_amount)

if purchase_amount > 2000:
    print("Delivery Charge: 0")
else:
    print("Delivery Charge:",delivery_charge)

if customer_type == "premium":
    print("Final Bill:",final_bill_P)
else:
    print("Final Bill:",final_bill_R)



'''
Smart Electricity Bill Calculator
'''

name = input("Enter Your Name: ")
units = float(input("How many units consumed: "))
service_charged = 150

# Validate units and calculate energy charge
if units < 0:
    print("Wrong Units Information")

else:
    # Calculate energy charge
    if units <= 100:
        energy_charged = units * 3

    elif units <= 200:
        energy_charged = units * 5 - 200

    else:
        energy_charged = units * 7 - 400 - 200

    # Calculate final bill
    final_bill = energy_charged + service_charged

    # Display usage message
    if final_bill > 5000:
        usage_message = "High Usage Bill and Units Consumption"
    else:
        usage_message = "Normal Usage"

    # Display electricity bill
    print("\n===== ELECTRICITY BILL =====")
    print("Customer Name:", name)
    print("Units Consumed:", units)
    print("Energy Charge: ₹", energy_charged)
    print("Service Charge: ₹", service_charged)
    print("Final Bill: ₹", final_bill)
    print("Usage Message:", usage_message)
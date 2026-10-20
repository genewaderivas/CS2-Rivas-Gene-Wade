# Electricity Bill Calculator
RATE = 12.90

#Validate if the user input his name
name = input("Enter customer name: ")


if name.strip() == "":
    print("Name is not given. Pls input it!")
    name = input("Enter customer name: ")


#Validate if the previous reading is at least zero
previous = float(input("Enter previous meter reading: "))

if previous < 0:
    print("Previous reading must be at least 0!")
    previous = float(input("Enter previous meter reading: "))


#Validate if the current reading is at least the previous reading
current = float(input("Enter current meter reading: "))

if current < previous:
    print("Current reading must be at least the previous reading!")
    current = float(input("Enter current meter reading: "))




consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading

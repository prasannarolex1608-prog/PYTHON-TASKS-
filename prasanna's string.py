'''1. Coffee Shop Ordering System (Basic)
Scenario:
You are developing a simple ordering system for a new coffee shop. The system needs to calculate the total bill for a customer's order and apply a discount if applicable. 
Task:
Create a Python program that performs the following actions:
Display a menu with item names and prices (e.g., Coffee: $3.50, Muffin: $2.00, Bagel: $4.00).
Prompt the user to select items and quantities.
Calculate the total cost of the order.
Apply a 10% discount if the total bill exceeds $20.00.
Display the final amount payable. '''

Coffee_price=3.50
Muffin_price=2.00
Bagel_price=4.00

print("Menu")
print("Coffee: $3.50")
print("Muffin: $2.00")
print("Bagel:  $4.00")

Coffee_qty=int(input("Enter number of coffee's:"))
Muffin_qty=int(input("Enter number of Muffin's:"))
Bagel_qty=int(input("Enter number of Bagel's:"))

Bill=(Coffee_qty*Coffee_price)+(Muffin_qty*Muffin_price)+(Bagel_qty*Bagel_price)
print(Bill)

if Bill>20.00:
    discount=Bill*0.10
else:
 discount=0
 

total_bill=Bill-discount
print("Total bill",total_bill)


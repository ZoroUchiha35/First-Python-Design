#This is me first program
print("Hello, Welcome to our Barista Hotel!!!")

name = input("What's your name: ")
while name == "":
    name = input("What's your name: ")
print(f"Hello {name}, thank you for coming in today\nHere is our Menu\n")

# Define menu items
drinks = ("Coffee", "Soda", "Milk")
food = ("Chapati", "Ugali", "Mchele")
takeaway = ("Chips", "Kuku", "Kebab")

# Display categories
print("MENU")
print("\nDRINKS:")
for i, item in enumerate(drinks, 1):
    print(f"  {i}. {item}")

print("\nFOOD:")
for i, item in enumerate(food, 1):
    print(f"  {i}. {item}")

print("\nTAKEAWAY:")
for i, item in enumerate(takeaway, 1):
    print(f"  {i}. {item}")

# Category selection
print("\nSelect a category:")
print("1. Drinks")
print("2. Food")
print("3. Takeaway")

category = input("\nEnter category number (1-3): ")

# Process selection
if category == "1":
    print("\nYou selected Drinks:")
    for i, item in enumerate(drinks, 1):
        print(f"  {i}. {item}")
    item_choice = input("\nSelect drink (1-3): ")
    if item_choice in ["1", "2", "3"]:
        selected_item = drinks[int(item_choice) - 1]
        print(f"\nYou selected: {selected_item}")
        print(f"Thank you {name}! Your order has been placed.")
    else:
        print("Invalid selection!")

elif category == "2":
    print("\nYou selected Food:")
    for i, item in enumerate(food, 1):
        print(f"  {i}. {item}")
    item_choice = input("\nSelect food (1-3): ")
    if item_choice in ["1", "2", "3"]:
        selected_item = food[int(item_choice) - 1]
        print(f"\nYou selected: {selected_item}")
        print(f"Thank you {name}! Your order has been placed.")
    else:
        print("Invalid selection!")

elif category == "3":
    print("\nYou selected Takeaway:")
    for i, item in enumerate(takeaway, 1):
        print(f"  {i}. {item}")
    item_choice = input("\nSelect takeaway (1-3): ")
    if item_choice in ["1", "2", "3"]:
        selected_item = takeaway[int(item_choice) - 1]
        print(f"\nYou selected: {selected_item}")
        print(f"Thank you {name}! Your order has been placed.")
    else:
        print("Invalid selection!")

else:
    print("Invalid category selection!")





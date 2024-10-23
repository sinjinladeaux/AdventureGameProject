import gamefunctions

# Get the player's name
player_name = input("Enter your name: ")
print(f"Hello, {player_name}!")

# Print the welcome message and shop menu
gamefunctions.print_welcome()
gamefunctions.print_shop_menu()

# Ask the player what item they want to purchase
item = input("What would you like to buy? ")
gold = int(input("How much gold do you have? "))
purchase_result = gamefunctions.purchase_item(item, gold)
print(purchase_result)

# Encounter a random monster
print(f"Watch out, {player_name}, a wild {gamefunctions.random_monster()} appears!")

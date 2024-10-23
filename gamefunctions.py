#gamefunctions.py
#Sinjin LaDeaux
#10/20/2024

import random

def print_welcome(name, width=20):
    print(f"{'Hello, ' + name + '!':^{width}}")

# Calling print_welcome() three times with different inputs
print_welcome("Jeff")
print_welcome("Sinjin")
print_welcome("Stranger")

def print_shop_menu(item1Name, item1Price, item2Name, item2Price):

    print("/" + "-"*22 + "\\")
    print(f"| {item1Name:<12} ${item1Price:>7.2f} |")
    print(f"| {item2Name:<12} ${item2Price:>7.2f} |")
    print("\\" + "-"*22 + "/")

# Calling print_shop_menu() three times with different inputs
print_shop_menu("Apple", 31, "Pear", 1.234)
print_shop_menu("Egg", 0.23, "Bag of Oats", 12.34)
print_shop_menu("Banana", 0.99, "Orange", 3.75)

def purchase_item():
    # Randomly selecting an item and its price
    items = {
        "Sword": round(random.uniform(10, 50), 2),
        "Shield": round(random.uniform(15, 45), 2),
        "Potion": round(random.uniform(2, 10), 2),
        "Armor": round(random.uniform(30, 100), 2),
        "Boots": round(random.uniform(5, 25), 2)
    }
    
    # Select a random item from the list
    item_name = random.choice(list(items.keys()))
    item_price = items[item_name]

    # Randomly generate starting money for the user
    starting_money = round(random.uniform(20, 100), 2)  # Random money between $20 and $100

    # Randomly generate quantity to purchase (between 1 and 5)
    quantity_to_purchase = random.randint(1, 5)

    # Show the item being bought and the price
    print(f"\nItem for sale: {item_name}")
    print(f"Price of each {item_name}: ${item_price:.2f}")
    print(f"Available money: ${starting_money:.2f}")
    print(f"Quantity to purchase: {quantity_to_purchase}")
    
    # Calculate the number of items that can be purchased
    max_affordable_items = int(starting_money // item_price)
    items_purchased = min(max_affordable_items, quantity_to_purchase)
    
    # Calculate the remaining money after the purchase
    leftover_money = starting_money - (items_purchased * item_price)
    
    # Display the results
    print(f"\nItems purchased: {items_purchased} {item_name}(s)")
    print(f"Money left: ${leftover_money:.2f}\n")
    
    return items_purchased, leftover_money

# Run the function three times to test
if __name__ == "__main__":
    for i in range(3):
        print(f"Purchase attempt {i+1}:")
        purchase_item()
        print("-" * 30)  # Divider between attempts


def new_random_monster():
    # Define monster types with their specific attributes
    monster_types = {
        "Goblin": {
            "description": "A lone goblin. When it notices you, it rushes at you quickly with a sharp dagger drawn.",
            "health_range": (10, 30),
            "power_range": (5, 15),
            "money_range": (5, 50)
        },
        "Orc": {
            "description": "A brutish orc wielding a heavy axe. It roars a challenge as it spots you.",
            "health_range": (30, 60),
            "power_range": (10, 25),
            "money_range": (20, 100)
        },
        "Vulture": {
            "description": "You discover a vulture eating the remains of two orcs that appear to have killed each other. They were carrying a chest that contains a small treasure horde.",
            "health_range": (1, 5),
            "power_range": (1, 3),
            "money_range": (50, 200)
        }
    }

    # Randomly choose a monster type
    monster_name = random.choice(list(monster_types.keys()))
    monster_info = monster_types[monster_name]

    # Generate random values for health, power, and money
    health = random.uniform(*monster_info["health_range"])
    power = random.uniform(*monster_info["power_range"])
    money = random.uniform(*monster_info["money_range"])

    # Create and return the monster dictionary
    return {
        "name": monster_name,
        "description": monster_info["description"],
        "health": round(health, 2),
        "power": round(power, 2),
        "money": round(money, 2)
    }

# Test the function
if __name__ == "__main__":
    for _ in range(3):
        monster = new_random_monster()
        print(f"Name: {monster['name']}")
        print(f"Description: {monster['description']}")
        print(f"Health: {monster['health']}")
        print(f"Power: {monster['power']}")
        print(f"Money: {monster['money']}")
        print("-" * 50)


import random
from gamefunctions import new_random_monster

def display_menu(current_hp, current_gold):
    """Display the main game menu with current stats."""
    print(f"Current HP: {current_hp}, Current Gold: {current_gold}")
    print("What would you like to do?\n")
    print("1) Fight Monster")
    print("2) Sleep (Restore HP for 5 Gold)")
    print("3) Quit")

def get_user_choice():
    """Get and validate user input for main menu."""
    while True:
        choice = input("Enter your choice (1-3): ")
        if choice in ['1', '2', '3']:
            return int(choice)
        print("Invalid choice. Please enter a number between 1 and 3.")

def display_fight_statistics(player_hp, monster):
    """Display current fight statistics."""
    print(f"\nYour HP: {player_hp:.1f}")
    print(f"{monster['name']} HP: {monster['health']:.1f}")

def get_fight_choice():
    """Get and validate user input during fight."""
    while True:
        print("\n1) Continue Fighting")
        print("2) Run Away")
        choice = input("Enter your choice (1-2): ")
        if choice in ['1', '2']:
            return int(choice)
        print("Invalid choice. Please enter 1 or 2.")

def process_combat_round(current_hp, monster):
    """Process one round of combat."""
    player_damage = random.randint(5, 15)
    monster_damage = round(random.uniform(1, monster['power']), 2)
    
    monster['health'] -= player_damage
    current_hp -= monster_damage
    
    print(f"\nYou dealt {player_damage} damage to the {monster['name']}.")
    print(f"The {monster['name']} dealt {monster_damage} damage to you.")
    
    return current_hp, monster['health']

def fight_monster(current_hp, current_gold):
    """Handle the monster fight sequence."""
    monster = new_random_monster()
    print(f"\nA {monster['name']} appears!")
    print(monster['description'])
    
    while current_hp > 0 and monster['health'] > 0:
        display_fight_statistics(current_hp, monster)
        
        current_hp, monster_health = process_combat_round(current_hp, monster)
        
        if monster['health'] <= 0:
            print(f"\nYou defeated the {monster['name']}!")
            current_gold += monster['money']
            print(f"You found {monster['money']:.2f} gold!")
            return current_hp, current_gold
            
        if current_hp <= 0:
            return current_hp, current_gold
            
        if get_fight_choice() == 2:
            print("You ran away!")
            gold_lost = round(random.uniform(1, 5), 2)
            current_gold = max(0, current_gold - gold_lost)
            print(f"You dropped {gold_lost:.2f} gold while running!")
            break
            
    return current_hp, current_gold

def sleep(current_hp, current_gold):
    """Handle the sleep/rest mechanic."""
    if current_gold >= 5:
        current_hp += 10
        current_gold -= 5
        print("\nYou slept and restored 10 HP.")
        print("It cost you 5 gold.")
    else:
        print("\nNot enough gold to sleep!")
    return current_hp, current_gold

def main():
    """Main game loop."""
    current_hp = 30
    current_gold = 10
    
    while True:
        display_menu(current_hp, current_gold)
        choice = get_user_choice()
        
        if choice == 1:
            current_hp, current_gold = fight_monster(current_hp, current_gold)
            if current_hp <= 0:
                print("\nYou have been defeated!")
                break
        elif choice == 2:
            current_hp, current_gold = sleep(current_hp, current_gold)
        else:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()

#Sinjin LaDeaux
#items.py
#11/3/2024

class Item:
    def __init__(self, name, item_type, **kwargs):
        self.name = name
        self.type = item_type
        for key, value in kwargs.items():
            setattr(self, key, value)

class Inventory:
    def __init__(self):
        self.items = []
        self.equipped = {
            "weapon": None,
            "shield": None,
            "misc": None
        }
    
    def add_item(self, item):
        """Add an item to inventory"""
        self.items.append(item)
    
    def get_items_by_type(self, item_type):
        """Return list of items of specified type"""
        return [item for item in self.items if item.type == item_type]
    
    def equip_item(self, item):
        """Equip an item of its type"""
        if item in self.items:
            self.equipped[item.type] = item
            return True
        return False
    
    def use_item(self, item):
        """Use an item, handle durability and removal if necessary"""
        if item not in self.items:
            return False
            
        if hasattr(item, 'currentDurability'):
            item.currentDurability -= 1
            if item.currentDurability <= 0:
                self.items.remove(item)
                if self.equipped[item.type] == item:
                    self.equipped[item.type] = None
                return True
        return True

def create_shop_items():
    """Create the initial shop items"""
    return [
        {
            "name": "Sword",
            "type": "weapon",
            "maxDurability": 10,
            "currentDurability": 10,
            "damage_bonus": 5,
            "price": 20
        },
        {
            "name": "Monster Charm",
            "type": "misc",
            "price": 30,
            "description": "Use to instantly defeat one monster"
        }
    ]

def purchase_item(inventory, item_data, current_gold):
    """Purchase an item and add it to inventory"""
    if current_gold >= item_data["price"]:
        item = Item(item_data["name"], item_data["type"], **{k:v for k,v in item_data.items() 
                                                            if k not in ["name", "type", "price"]})
        inventory.add_item(item)
        return current_gold - item_data["price"], True
    return current_gold, False

def display_inventory(inventory):
    """Display the current inventory"""
    print("\nInventory:")
    for item in inventory.items:
        equipped_status = " (Equipped)" if inventory.equipped[item.type] == item else ""
        durability_status = f" - Durability: {item.currentDurability}/{item.maxDurability}" if hasattr(item, 'currentDurability') else ""
        print(f"- {item.name} ({item.type}){equipped_status}{durability_status}")

def equip_menu(inventory, item_type):
    """Display equip menu for specific item type"""
    items = inventory.get_items_by_type(item_type)
    if not items:
        print(f"\nNo {item_type}s available to equip.")
        return False
        
    print(f"\nAvailable {item_type}s to equip:")
    for i, item in enumerate(items, 1):
        print(f"{i}) {item.name}")
    print(f"{len(items) + 1}) None")
    
    while True:
        try:
            choice = int(input(f"Choose {item_type} to equip (1-{len(items) + 1}): "))
            if 1 <= choice <= len(items):
                inventory.equip_item(items[choice - 1])
                print(f"Equipped {items[choice - 1].name}")
                return True
            elif choice == len(items) + 1:
                inventory.equipped[item_type] = None
                print(f"Unequipped {item_type}")
                return True
        except ValueError:
            pass
        print("Invalid choice. Please try again.")

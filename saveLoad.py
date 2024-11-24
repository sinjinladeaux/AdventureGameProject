import json
import os
from items import Item, Inventory

def save_game(player_name, current_hp, current_gold, inventory, filename=None):
    """Save game state to a JSON file"""
    if filename is None:
        filename = f"save_{player_name.lower()}.json"
    
    # Create save data dictionary
    save_data = {
        "player_name": player_name,
        "current_hp": current_hp,
        "current_gold": current_gold,
        "inventory": {
            "items": [],
            "equipped": {
                "weapon": None,
                "shield": None,
                "misc": None
            }
        }
    }
    
    # Save inventory items
    for item in inventory.items:
        item_data = {
            "name": item.name,
            "type": item.type
        }
        # Save additional attributes (like durability)
        for attr in vars(item):
            if attr not in ["name", "type"]:
                item_data[attr] = getattr(item, attr)
        save_data["inventory"]["items"].append(item_data)
    
    # Save equipped items
    for slot, item in inventory.equipped.items():
        if item is not None:
            save_data["inventory"]["equipped"][slot] = item.name
    
    # Save to file
    with open(filename, 'w') as f:
        json.dump(save_data, f, indent=4)
    
    print(f"\nGame saved to {filename}")
    return filename

def load_game(filename):
    """Load game state from a JSON file"""
    try:
        with open(filename, 'r') as f:
            save_data = json.load(f)
        
        # Create new inventory
        inventory = Inventory()
        
        # Load items
        for item_data in save_data["inventory"]["items"]:
            name = item_data.pop("name")
            item_type = item_data.pop("type")
            item = Item(name, item_type, **item_data)
            inventory.add_item(item)
        
        # Restore equipped items
        for slot, item_name in save_data["inventory"]["equipped"].items():
            if item_name is not None:
                for item in inventory.items:
                    if item.name == item_name:
                        inventory.equipped[slot] = item
                        break
        
        return (
            save_data["player_name"],
            save_data["current_hp"],
            save_data["current_gold"],
            inventory
        )
    
    except FileNotFoundError:
        print(f"Save file {filename} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error reading save file {filename}.")
        return None
    except KeyError as e:
        print(f"Save file {filename} is corrupted or incompatible.")
        return None

def list_save_files():
    """List all available save files in the current directory"""
    save_files = [f for f in os.listdir() if f.startswith("save_") and f.endswith(".json")]
    return save_files

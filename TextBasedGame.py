# Name: Christopher Sanders
# IT 140 Project Two - Museum Heist Text Adventure Game

def show_instructions():
    """Display game instructions and available commands"""
    print("=" * 60)
    print("Museum Heist Text Adventure Game")
    print("=" * 60)
    print("You are a master thief attempting to steal 6 priceless artifacts")
    print("from the Metropolitan Museum of Art.")
    print("Collect all 6 items before the Head of Security catches you!")
    print()
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")
    print("=" * 60)


def show_status(current_room, inventory, rooms):
    """Display player's current status including room, inventory, and available item"""
    print()
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")
    
    # Check if there's an item in the current room
    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    
    print("-" * 30)


def main():
    """Main game function containing the gameplay loop"""
    
    # Dictionary linking rooms to other rooms and items
    rooms = {
        'Grand Lobby': {'North': 'Egyptian Wing', 'East': 'Greek Gallery', 'South': 'Medieval Hall', 'West': 'Asian Art Room'},
        'Egyptian Wing': {'South': 'Grand Lobby', 'East': 'Renaissance Gallery', 'item': 'Ancient Scarab'},
        'Greek Gallery': {'West': 'Grand Lobby', 'North': 'Renaissance Gallery', 'item': 'Golden Amphora'},
        'Medieval Hall': {'North': 'Grand Lobby', 'item': 'Royal Crown'},
        'Asian Art Room': {'East': 'Grand Lobby', 'item': 'Jade Dragon'},
        'Renaissance Gallery': {'South': 'Egyptian Wing', 'West': 'Greek Gallery', 'East': 'Security Office', 'item': 'Diamond Painting'},
        'Security Office': {'West': 'Renaissance Gallery', 'item': 'Head of Security'}
    }
    
    # Initialize game variables
    current_room = 'Grand Lobby'
    inventory = []
    total_items = 6
    
    show_instructions()
    
    # Main gameplay loop
    while True:
        show_status(current_room, inventory, rooms)
        
        if current_room == 'Security Office':
            if len(inventory) < total_items:
                print()
                print("=" * 60)
                print("The Head of Security has caught you!")
                print("BUSTED! GAME OVER!")
                print("=" * 60)
                print("Thanks for playing the game. Hope you enjoyed it.")
                break
            else:
                print()
                print("=" * 60)
                print("Congratulations! You have collected all the artifacts")
                print("and successfully escaped the museum!")
                print("You are the ultimate master thief!")
                print("=" * 60)
                print("Thanks for playing the game. Hope you enjoyed it.")
                break
        
        command = input("Enter your move: ").strip()
        
        command_lower = command.lower()
        
        command_parts = command_lower.split()
        
        # Process movement commands
        if len(command_parts) >= 2 and command_parts[0] == 'go':
            direction = command_parts[1].capitalize()
            
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way! Try a different direction.")
        
        # Process get item commands
        elif len(command_parts) >= 2 and command_parts[0] == 'get':
            item_name = ' '.join(command_parts[1:]).title()
            
            if 'item' in rooms[current_room]:
                room_item = rooms[current_room]['item']
                
                if item_name.lower() == room_item.lower():
                    if room_item not in inventory:
                        inventory.append(room_item)
                        print(f"You picked up the {room_item}!")
                        
                        del rooms[current_room]['item']
                        
                        if len(inventory) == total_items:
                            print()
                            print("You've collected all the artifacts!")
                            print("Now escape through the Security Office!")
                    else:
                        print("You already have that item!")
                else:
                    print(f"That item is not here. Try 'get {room_item}'.")
            else:
                print("There is no item in this room to collect.")
        
        # Invalid command
        else:
            print("Invalid command! Use 'go [direction]' or 'get [item name]'.")


# Run the main game function
if __name__ == "__main__":
    main()
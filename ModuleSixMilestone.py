# IT 140 Module Six Milestone

# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

current_room = 'Great Hall'

# Display game instructions
print('Welcome to the Dragon Text Game!')
print('Move commands: go South, go North, go East, go West')
print('To exit the game, type: exit')
print('-' * 40)

# Main gameplay loop
while current_room != 'exit':
    print(f'\nYou are in the {current_room}')
    
    command = input('Enter your move: ').strip()
    
    command_lower = command.lower()
    
    if command_lower == 'exit':
        current_room = 'exit'
        continue
    
    if command_lower.startswith('go '):
        direction = command[3:].strip().capitalize()
        
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way! Try a different direction.")
    else:
        print('Invalid move! Please use format: go [direction] or exit')

# Game over message
print('\nThanks for playing the game. Hope you enjoyed it!')
print('\nYour Items:')
inventory = ['sword', 'armor', 'sheild', 'healing potion']
for item in inventory:
    print(item)

input('\nPress the enter key to continue.')
print(f'\nYou have {len(inventory)} items in your possession.')

input('\nPress the enter key to continue.')
if 'healing potion' in inventory:
    print('\nYou will live to fight another day.')

item = int(input('\nEnter the index number for an item in your inventory: '))
print(f'At index {item} is {inventory[item]}')

fir = int(input('\nEnter the index number to begin a slice: '))
sec = int(input('Enter the index number to end a slice: '))
print(f'Inventory[{fir}:{sec}] is {inventory[fir:sec]}')
input('\nPress the enter key to continue.')
chest = ['gold', 'gems']
print('\nYou find a chest which contains:')
print(chest)
print('You add the contents of the chest to your inventory.')
inventory += chest
print('Your inventory is now: ')
print(inventory)
input('\nPress the enter key to continue.')
inventory[0] = 'crossbow'
print('\nYou trade your sword for a crossbow.')
print('Your inventory is now: ')
print(inventory)
input('\nPress the enter key to continue.')
inventory[4:6] = ['Orb of future telling']
print('\nYou use your gold and gems to buy an orb of future telling.')
print('Your inventory is now:')
print(inventory)
input('\nPress the enter key to continue.')
del inventory[2]
print('\nIn a great battle your shield is destroyed.')
print('Your inventory is now:')
print(inventory)
input('\nPress the enter key to continue.')
del inventory[0:1]
print('\nYour crossbow and armor are stolen by theives.')
print('Your inventory is now:')
print(inventory)
print('\n\n')
input('Press the enter key to exit.')

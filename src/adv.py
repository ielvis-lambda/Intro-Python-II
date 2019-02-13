from room import Room
from item import Item
from player import Player

# Declare all the rooms
room = {
	'outside':  Room("Outside Cave Entrance",
					 "North of you, the cave mount beckons",[Item("Stick", "a dirty stick")]),

	'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Rope", "a long rope")]),

	'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Spoon", "a wooden spoon")]),

	'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Lantern", "a glowing lantern")]),

	'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Gold Coin", "a shiny gold coin")]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
e = Player("Elvis", "outside")

# Write a loop that:
#
# * Prints the current room name
print(f"{e.name}'s location is {e.room}")
# * Prints the current description (the textwrap module might be useful here).
for i in room:
	# print(e.room)
	# print(room[i])
	if i == e.room:
		print(room[i].prompt)
# * Waits for user input and decides what to do.

# passing in the direction
# while True: 

	dir = input(">> ")

# If the user enters a cardinal direction, attempt to move to the room there.
	if dir == 'n':
		print(e.room)
		print(room[e.room].n_to.name)

		e.room = room[e.room].n_to.name

		print(f"{e.name}'s location is: {e.room}")


	elif dir == 's':
		e.room == room['{e.room}'].s
	elif dir == 'w':
		e.room == room['{e.room}'].e
	elif dir == 'e':
		e.room == room['{e.room}'].w
# Print an error message if the movement isn't allowed.
# print(f"{e.name} is {e.room}")
# If the user enters "q", quit the game.

# print(f"{room['outside'].n_to}")

# a = "fish"

# print(a)

# print(room["foyer"].name)

# print(room['outside'].n_to.name)
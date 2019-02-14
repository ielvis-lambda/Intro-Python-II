from room import Room
from item import Item
from player import Player

# Declare all the rooms
room = {
	'outside':  Room("Outside Cave Entrance",
					 "North of you, the cave mount beckons", [Item("Stick", "a dirty stick")]),

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

# print(room[e.room].s_to)
# print([k for k, v in room.items() if v == "Outside Cave Entrance"])

# print(room[e.room].name)

oce = room[e.room].name

# for r in room:
#     print(room.get(r).name)
#     if room.get(r).name == oce:
#         print(f"this one is equal! {room.get(r).name}")
#     else:
#         print("no match")

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


def game():

	print("Move! Enter 'n', 's', 'e' or 'w' to move. 'q' to quit.")

	while True:

		dir = input(">> ")

	# If the user enters a cardinal direction, attempt to move to the room there.

		if dir == 'n':				
			print(room[e.room].name)
			for r in room:
				# print(room.get(r).name)
				try:
					room[e.room].n_to.name
					print(f"this one is equal! {room.get(r).name}")
					room[e.room] = room[e.room].n_to
					print(f"{e.name}'s location is: {room[e.room].name}")
					break
				except AttributeError:
					print(f"dir is {dir}")
					print("A strong force blocks your path")
					# print(f"{e.name}'s location is: {e.room.name}")
					break
		elif dir == 's':				
			print(room[e.room].name)
			for r in room:
				# print(room.get(r).name)
				try:
					room[e.room].s_to.name
					print(f"this one is equal! {room.get(r).name}")
					room[e.room] = room[e.room].s_to
					print(f"{e.name}'s location is: {room[e.room].name}")
					break
				except AttributeError:
					print(f"dir is {dir}")
					print("A strong force blocks your path")
					# print(f"{e.name}'s location is: {e.room.name}")
					break		
		elif dir == 'e':				
			print(room[e.room].name)
			for r in room:
				# print(room.get(r).name)
				try:
					room[e.room].e_to.name
					print(f"this one is equal! {room.get(r).name}")
					room[e.room] = room[e.room].e_to
					print(f"{e.name}'s location is: {room[e.room].name}")
					break
				except AttributeError:
					print(f"dir is {dir}")
					print("A strong force blocks your path")
					# print(f"{e.name}'s location is: {e.room.name}")
					break	
		elif dir == 'w':				
			print(room[e.room].name)
			for r in room:
				# print(room.get(r).name)
				try:
					room[e.room].w_to.name
					print(f"this one is equal! {room.get(r).name}")
					room[e.room] = room[e.room].w_to
					print(f"{e.name}'s location is: {room[e.room].name}")
					break
				except AttributeError:
					print(f"dir is {dir}")
					print("A strong force blocks your path")
					# print(f"{e.name}'s location is: {e.room.name}")
					break	

	# If the user enters "q", quit the game.

	# print(f"{room['outside'].n_to}")

	# a = "fish"

	# print(a)

	# print(room["foyer"].name)

	# print(room['outside'].n_to.name)
if __name__ == '__main__':
	game()

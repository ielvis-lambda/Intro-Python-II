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
e = Player("Elvis", "outside", [])

# Inventory Testing


def getItem():
	items = sorted(room[e.room].items)
	print(e.inventory)
	for i in items:
		print(i.name)
		e.inventory.append(i.name)
		print(e.inventory)


# getItem()

# Write a loop that:

# * Prints the current room name
print(f"{e.name}'s location is {e.room}")

items = sorted(room[e.room].items)

# for i in items:
#     print(i.name)

# print(f"{e.name}'s location is {items}")

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

		# count the arguments & start at items to use args as items
		args = dir.split()[1:]
		numargs = len(args) + 1

	# If the user enters a cardinal direction, attempt to move to the room there.

		if dir == 'n':
			print(room[e.room].name)
			for r in room:
				# print(room.get(r).name)
				try:
					room[e.room].n_to.name
					room[e.room] = room[e.room].n_to
					items = sorted(room[e.room].items)
					print(f"{room[e.room].prompt}")
					for i in items:
						print(f"You see a {i.name} in the room")
					break
				except AttributeError:
					print(f"dir is {dir}")
					print("A strong force blocks your path")
					break
		elif dir == 's':
			print(room[e.room].name)
			for r in room:
				# print(room.get(r).name)
				try:
					room[e.room].s_to.name
					room[e.room] = room[e.room].s_to
					items = sorted(room[e.room].items)
					print(f"{room[e.room].prompt}")
					for i in items:
						print(f" You see a {i.name} in the room")
					break
				except AttributeError:
					print(f"dir is {dir}")
					print("A strong force blocks your path")
					break
		elif dir == 'e':
			print(room[e.room].name)
			for r in room:
				# print(room.get(r).name)
				try:
					room[e.room].e_to.name
					room[e.room] = room[e.room].e_to
					items = sorted(room[e.room].items)
					print(f"{room[e.room].prompt}")
					for i in items:
						print(f" You see a {i.name} in the room")
					break
				except AttributeError:
					print(f"dir is {dir}")
					print("A strong force blocks your path")
					break
		if dir == 'w':
			print(room[e.room].name)
			for r in room:
				# print(room.get(r).name)
				try:
					room[e.room].w_to.name
					room[e.room] = room[e.room].w_to
					items = sorted(room[e.room].items)
					print(f"{room[e.room].prompt}")
					for i in items:
						print(f" You see a {i.name} in the room")
					break
				except AttributeError:
					print(f"dir is {dir}")
					print("A strong force blocks your path")
					break

	# If the user enters "q", quit the game.

		elif dir == 'q':
			print("Goodbye")
			# print(f"{e.name}'s location is: {e.room.name}")
			break

		elif dir.startswith("get "):
			items = sorted(room[e.room].items)
			print(f"the number of items you are trying to get is {numargs}")
			if int(numargs) > 2:
				error = "You may only get 1 item at a time."
				print(error)
			else:
				item = args[0]
				for i in items:
					if str(i.name) == str(item):
						print(f"Your inventory is: {e.inventory}")
						print(f"you picked up {item}")
						e.inventory.append(Item(i.name, i.description))
						print(f"Your inventory is now: {e.inventory}")
						for i in room[e.room].items:
							print(i.name)
							for item in room[e.room].items:
								print(f"item in room is {item.name}")
								if str(i.name) == str(item.name):
									print(
										f"The items in the room are: {room[e.room].items}")
									room[e.room].items.remove(item)
									print(
										f"The items in the room are now: {room[e.room].items}")
									item.on_take()
					else:
						print(f"{item} is not in the room")
						pass

		elif dir == "i":
			if len(e.inventory) < 1:
				print("Your inventory is empty")
			else:
				print("You have the following items in your inventory:")
				for i in e.inventory:
					print(i.name)


		elif dir.startswith("drop "):
			items = sorted(e.inventory)
			print(f"the number of items you are trying to drop is {numargs}")
			if int(numargs) > 2:
				error = "You may only drop 1 item at a time."
				print(error)
			else:
				item = args[0]
				for i in items:
					if str(i.name) == str(item):
						print(f"Your inventory is: {e.inventory}")
						print(f"you dropped {item}")
						e.inventory.remove(item)
						print(f"Your inventory is now: {e.inventory}")
						for i in room[e.room].items:
							print(i.name)
							for item in room[e.room].items:
								print(f"item in room is {item.name}")
								if str(i.name) == str(item.name):
									print(
										f"The items in the room are: {room[e.room].items}")
									room[e.room].items.append(item)
									print(
										f"The items in the room are now: {room[e.room].items}")
									item.on_take()
					else:
						print(f"{item} is not in your inventory")
						pass



if __name__ == '__main__':
	game()

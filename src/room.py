# Implement a class to hold room information. This should have name and
# description attributes.

class Room: 
	def __init__(self, name, prompt, items):
		self.name = name
		self.prompt = prompt
		self.items = items

	def addItem(self, i):
		print(f"Picked up {self.items[i]}!")


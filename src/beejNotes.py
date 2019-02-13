# Is-a: inheritance
# Has-a: composition

class WheeledVehicle:   # "Base class", "Super class", "Parent class"
	def __init__(self, name, num_wheels):
		self.name = name
		self.num_wheels = num_wheels 

	def drive(self):
		print(f"{self.name} is driving!")

# motorcycle has an is-a relationship with WheeledVehicle
class Motorcycle(WheeledVehicle):   # "Derived class", "specialized", "sub class", "child class"
	def __init__(self, name):
		super().__init__(name, 2)

	def drive(self):     # Method overriding
		super().drive()
		print("Brrraaaapp!")

class Car(WheeledVehicle):
	def __init__(self, name):
		super().__init__(name, 4)

		self.seat = Seat()   # Car has-a seat

class Seat():
	def recline(self):
		pass

c = Car("Adventuremobile")  # c is an instance of Car

c.seat.recline()

c.drive()

m = Motorcycle("Jackie")

m.drive()
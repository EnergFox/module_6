class Animal:
	def __int__(self, speed, _cords):
		self.live = True
		self.sound = None
		self._DEGREE_OF_DANGER = 0
		self._cords = [0, 0, 0]
		self.speed = speed

	def move(self, dx, dy, dz):
		self._cords[0] = dx * self.speed
		self._cords[1] = dy * self.speed
		self._cords[2] = dz * self.speed
		if self._cords[2] <= -1:
			print("It's too deep, i can't dive :(")
		else:
			return self._cords

	def get_cords(self):
		print(f'X:{self._cords[0]}, Y:{self._cords[1]}, Z:{self._cords[2]}')

	def attack(self):
		if self._DEGREE_OF_DANGER > 5:
			print("Sorry, i'm peaceful :)")
		elif self._DEGREE_OF_DANGER <= 5:
			print("Be careful, i'm attacking you 0_0")

	def speak(self):
		print(self.sound)

class Bird(Animal):
	beak = True

	def __init__(self, live):
		self.live = live

	def lay_eggs(self):
		import random
		random_number = random.randint(1, 4)
		print(f'Here are(is) {random_number} eggs for you')

class AquaticAnimal(Animal):
	def __init__(self, speed, _cords):
		self.speed = speed
		self._cords = [0, 0, 0]
	_DEGREE_OF_DANGER = 3


	def dive_in(self, dz):
		if dz <= 0:
			abs(dz)
		self._cords[2] = dz // self.speed
		return self._cords[0]




class PoisonousAnimal(Animal):
	_DEGREE_OF_DANGER = 8



class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
	sound = "Click-click-click"
	def __init__(self, speed):
		AquaticAnimal.__init__(self, speed, _cords=[0, 0, 0])
		Bird.__init__(self, live=True)




db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()



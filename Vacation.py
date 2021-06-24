#Lukas Robin
#21.06.2021
class Vacation(object):
	def __init__(self, gender, time, place):
		self.gender = gender
		self.time = time
		self.place = place
	def get_gender(self):
		return self.gender
	def get_time(self):
		return self.time
	def place(self):
		return self.place 
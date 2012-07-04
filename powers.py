class Power(object):
	def __init__(self):
		self.power_damage =  0
		self.power_cost = 0
		self.power_time = 0

	def set_rage(self, att):
		self.power_damage =  att * 4
		self.power_cost = 10
		self.power_time = 1

	def set_poison(self, att):
		self.power_damage = att / 2
		self.power_cost = 10
		self.power_time = 4

	def set_fireball(self, att):
		self.power_damage = 50
		self.power_cost = 40
		self.power_time = 0


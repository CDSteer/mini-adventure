import player
from player import * 
import mob
from mob import * 

class Rage(object):
	def __init__(self):
		self.power_damage = 20
		self.power_cost = 10
		self.power_time = 1
	
	def start_rage(att):
		return True

class Poison(object):
	def __init__(self):
		self.power_damage = 20
		self.power_cost = 10
		self.power_time = 4
	
	def start_poison(att):
		return True

class Fireball(object):
	def __init__(self):
		self.power_damage = 20
		self.power_cost = 40
		self.power_time = 0

import player
from player import * 
import mob
from mob import * 

class Rage(object):
	def __init__(self, att):
		self.power_damage =  att * 2
		self.power_cost = 10
		self.power_time = 1

class Poison(object):
	def __init__(self, att):
		self.power_damage = att / 2
		self.power_cost = 10
		self.power_time = 4

class Fireball(object):
	def __init__(self, att):
		self.power_damage = 20
		self.power_cost = 40
		self.power_time = 0

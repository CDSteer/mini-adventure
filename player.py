import powers
from powers import *

class Player(object):
	"""set up a players stats"""
	def __init__(self):
		self.plr_lvl = 0
		self.plr_XP = 0
		self.plr_maxXP = 50
		self.plr_name = " "
		self.plr_class = " "
		self.plr_power = " "
		self.plr_maxHP = 0
		self.plr_HP = 0
		self.plr_att = 0
		self.plr_def = 0
		self.plr_endu = 0
		self.plr_maxAP = 0
		self.plr_AP = 0
		self.poison = False
		self.rage = False
		
	def make_warrior(self, name):
		self.plr_lvl = 1
		self.plr_name = name
		self.plr_class = "Warrior"
		self.plr_power = "Rage"
		self.plr_maxHP = 300
		self.plr_HP = 300
		self.plr_att = 20
		self.plr_def = 30
		self.plr_endu = 10
		power = Rage(self.plr_att)
		max_AP = self.plr_endu * 2
		self.plr_maxAP = max_AP
		self.plr_AP = max_AP
	
	def make_rogue(self, name):
		self.plr_lvl = 1
		self.plr_name = name
		self.plr_class = "Rouge"
		self.plr_power = "Poison"
		self.plr_maxHP = 200
		self.plr_HP = 200
		self.plr_att = 30
		self.plr_def = 20
		self.plr_endu = 20
		power = Poison(self.plr_att)
		max_AP = self.plr_endu * 2
		self.plr_maxAP = max_AP
		self.plr_AP = max_AP
		
	def make_mage(self, name):
		self.plr_lvl = 1
		self.plr_name = name
		self.plr_class = "Mage"
		self.plr_power = "Fireball"
		self.plr_maxHP = 100
		self.plr_HP = 100
		self.plr_att = 10
		self.plr_def = 10
		self.plr_endu = 30
		power = Fireball(self.plr_att)
		max_AP = self.plr_endu * 2
		self.plr_maxAP = max_AP
		self.plr_AP = max_AP	
	
	"""check it the player is still alive retuen true for alive and false for dead"""
	def isalive(self, mob):
		if self.plr_HP <= 0:
			print "Game Over the %s brutaly murdereds you!" % mob
			return False
		else:
			return True
	
	def xp_check(self, mob_value):
		
		self.plr_XP = self.plr_XP + mob_value
		
		if self.plr_XP >= self.plr_maxXP:
			print "Level Up!!!"
			self.plr_lvl = self.plr_lvl + 1
			self.plr_maxXP = self.plr_maxXP * 3
			print "%s incresed to level %r" % (self.plr_name, self.plr_lvl)
			print "XP: %r/%r" % (self.plr_XP, self.plr_maxXP)
			"""Make function for upgrading stats"""
			return
		else:
			print "XP: %r/%r" % (self.plr_XP, self.plr_maxXP)
			return
	
			
	"""add get damage function"""
	
	
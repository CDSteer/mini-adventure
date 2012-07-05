import powers
from powers import *
import bag
from bag import *

power = Power()
bag = Bag()

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
		power.set_rage(self.plr_att)
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
		power.set_poison(self.plr_att)
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
		power.set_fireball(self.plr_att)
		max_AP = self.plr_endu * 2
		self.plr_maxAP = max_AP
		self.plr_AP = max_AP	
	
	"""check it the player is still alive retuen true for alive and false for dead"""
	def isalive(self):
		if self.plr_HP <= 0:
			self.print_HP()
			print "Game Over you were brutally murdered!"
			return False
		else:
			return True
	
	def power_use(self):
		print "%s uses %s" % (self.plr_name, self.plr_power)
		return power.power_damage
	
	def poison_damage(self, mob):
		if power.power_time == 3:
			mob.poison = False
			power.power_time = 0
			print "%s is no longer poisoned" %  mob
	
		print "%s is hurt by poison" % (mob)
		power.power_time + 1
		
		return power.power_damage
	
	def player_damage(self):
		dam = self.plr_att * 2
		return dam
	
	def player_defence(self, mob_dam):
		dam = mob_dam / self.plr_def
		return dam
		
	def damage_player(self, dam, mob):
		self.plr_HP = self.plr_HP - dam
		print "\n%s's attack deals %r points of damage" % (mob, dam)
		return
		
	def print_HP(self):
		print "Level %r %s: %r/%r\n" % (self.plr_lvl, self.plr_name, self.plr_HP, self.plr_maxHP)
		return
	
	def print_AP(self):
		print "2. %s Action Points: %r/%r" % (self.plr_power, self.plr_AP, self.plr_maxAP)
		return
	def print_AP2(self):
		print "Level %r %s: Action Points: %r/%r\n" % (self.plr_lvl, self.plr_name, self.plr_AP, self.plr_maxAP)
		return
		
	def AP_check(self):
		if self.plr_AP >= power.power_cost:
			return True
		else:
			print "Not Enough Action Points\n"
			return False
		
	def cost_AP(self):
		self.plr_AP = self.plr_AP - power.power_cost
		return
	
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
			
	def is_class(self, plr_class):
		if plr_class == self.plr_class:
			return True
			
	"""Functions for using items and the bag"""
	
	"""battle bag only displays items that can be used in battle"""
	def open_battle_bag(self):
		print "What item do you what to use?"
		print "1. HP Potion %r" % bag.id_01
		print "2. AP Potion %r" % bag.id_02
		print "3. Back"
		return
		
	def use_item(self, selected_item):
		
		if selected_item == "1":
			restore = bag.use_01()
			if restore == 100:
				self.plr_HP = self.plr_HP + restore
				if self.plr_HP > self.plr_maxHP:
					self.plr_HP = self.plr_maxHP
					self.print_HP()
					return
				else:
					self.print_HP()
					return True
			else:
				return False
		elif selected_item == "2":
			restore = bag.use_02()
			if restore == 100:
				self.plr_AP = self.plr_AP + restore
				if self.plr_AP > self.plr_maxAP:
					self.plr_AP = self.plr_maxAP
					self.print_AP2()
					return True
				else:
					self.print_AP2()
					return True
			else:
				return False

			
	
	
	
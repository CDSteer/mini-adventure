class Mob(object):		
	"""set up a mobs stats"""
	def __init__(self):
		self.mob_lvl = 0
		self.mob_name = ""
		self.mob_maxHP = 0
		self.mob_HP = 0
		self.mob_att = 0
		self.mob_def = 0
		self.mob_endu = 0
		self.poison = False
		self.rage = False
		self.mob_expValue = 0 
	
	"""checks if the mob is still alive, retuens true for alive and false for dead"""
	def is_alive(self):
		if self.mob_HP <= 0:
			return False
		else:
			return True
			
	def mob_damage(self):
		dam = self.mob_att * 2
		return dam
		
	def damage_mob(self, dam):
		self.mob_HP = self.mob_HP - dam
		print "You deal %r points of damage" % dam
		return
	
	def mob_defence(self, plr_dam):
		dam = plr_dam / self.mob_def
		return dam
	
	def print_HP(self):
		print "Level %r %s: %r/%r\n" % (self.mob_lvl, self.mob_name, self.mob_HP, self.mob_maxHP)
		return
	
	def poison_check(self):
		if self.poison == True:
			print "%s is all ready poisoned" % self.mob_name
			return True
		else:
			return False
	
	def make_mob(self, plr_lvl):
		
		if plr_lvl == 1:
			self.mob_lvl = 1
			self.mob_name = "Large Rat"
			self.mob_maxHP = 60
			self.mob_HP = 60
			self.mob_att = 30
			self.mob_def = 3
			self.mob_endu = 0
			self.mob_expValue = 50
			
		elif plr_lvl == 2:
			self.mob_lvl = 1
			self.mob_name = "Goblin"
			self.mob_maxHP = 60
			self.mob_HP = 60
			self.mob_att = 30
			self.mob_def = 5
			self.mob_endu = 0
			self.mob_expValue = 60
		elif plr_lvl == 3:
			self.Mob(2, "Troll", 60, 30, 10, 0, 50)
	
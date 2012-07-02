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
	
	def make_mob(self, plr_lvl):
		
		if plr_lvl == 1:
			self.mob_lvl = 1
			self.mob_name = "Large Rat"
			self.mob_maxHP = 60
			self.mob_HP = 60
			self.mob_att = 30
			self.mob_def = 10
			self.mob_endu = 0
			self.mob_expValue = 50
			
		elif plr_lvl == 2:
			self.mob_lvl = 1
			self.mob_name = "Goblin"
			self.mob_maxHP = 60
			self.mob_HP = 60
			self.mob_att = 30
			self.mob_def = 10
			self.mob_endu = 0
			self.mob_expValue = 60
		elif plr_lvl == 3:
			self.Mob(2, "Troll", 60, 30, 10, 0, 50)
	
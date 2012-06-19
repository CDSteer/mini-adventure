class Mob(object):		
	#set up a mobs stats
	def __init__(self, name, maxHP, HP, DP):
		self.name = name
		self.maxHP = maxHP
		self.HP = HP
		self.DP = DP
	
	#get the name of the mob
	def getmobname(self):
		return self.name
		
	#get the maxhp of the mob
	def getmobmaxHP(self):
		return self.maxHP
		
	#set the max hp of the mob
	def setmobmaxHP(self, newmax):
		self.maxHP = newmax
	
	#gets the mobs hp
	def getmobHP(self):
		return self.HP
	
	#sets a new hp for the mob
	def setmobHP(self, newhp):
		self.HP = newhp
	
	#gets the damge of the player
	def getmobDP(self):
		return self.DP
	
	#sets the damge of the player
#	in furture this will be calcalated from stats
	def setmobDP(self, newDP):
		self.DP = newDP

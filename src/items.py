class Items(object):	
	def __init__(self):
		self.item_name = " "
		self.item_class = " "
		self.item_power_bonus = 0
		self.item_att = 0
		self.item_endu = 0
		
	def make_03(self):
		self.item_name = "Short Sword"
		self.item_class = "Warrior"
		self.item_att = 5
		self.item_endu = 0
		self.item_power_bonus = 0
		
	def make_04(self):
		self.item_name = "Iron Dagger"
		self.item_class = "Rouge"
		self.item_att = 3
		self.item_endu = 0
		self.item_power_bonus = 3
		
	def make_05(self):
		self.item_name = "Wooden Staff"
		self.item_class = "Mage"
		self.item_att = 0
		self.item_endu = 10
		self.item_power_bonus = 0

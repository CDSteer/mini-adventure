import sys
import player
from player import * 
import mob
from mob import * 

print "Welcome Player, start by entering your name:"
name = raw_input(">")
print "Hello there %s, \nYou are about to enter a cave of no return." % name
print "Once inside the only way back a mistic portal at the end." 
print "So why take this risk? Because within this cave lies the worlds" 
print "largest collection of tresuse hiden away by a long dead king and" 
print "protected by evil monsters, so good luck :D"

print "Choose you class:"
print "1. Warrior: Power = Rage"
print "2. Thief:   Power = Poison"
print "3. Mage:    Power = Fireball"

plr_class = raw_input(">")

if plr_class == "1":
	#make the player setting the name, hp, dp depending on the class
	player = Player(1, name, "Warrior", "Rage", 300, 300, 20)
elif plr_class == "2":
	player = Player(1, name, "Thief", "Poison", 200, 200, 10)
elif plr_class == "3":
	player = Player(1, name, "Mage", "Fireball", 100, 100, 10)

print "Welcome %s" % player.plr_class

def user_attack():
	hp = mob.mob_HP
	dam = player.plr_DP
	new_hp = hp - dam
	mob.mob_HP = new_hp
	print "You deal %r points of damage" % player.plr_DP
	print "Level %r %s: %r/%r\n" % (mob.mob_lvl, mob.mob_name, mob.mob_HP, mob.mob_maxHP)
	return

def mob_attack():
	hp = player.plr_HP
	dam = mob.mob_DP
	new_hp = hp - dam
	player.plr_HP = new_hp
	print "\n%s deals %r points of damage" % (mob.mob_name, mob.mob_DP)
	print "Level %r %s: %r/%r\n" % (player.plr_lvl, player.plr_name, player.plr_HP, player.plr_maxHP)
	return
	
def battle():

	while mob.mob_HP > 0:
		if player.isalive(mob.mob_name) == False:
			sys.exit()
		print "How will you attack?"
		print "1. Basic Attack"
		print "2. %s" % player.plr_power
		print "3. Item"
		print "4. Quit"

		att_player = raw_input(">")
		
		if att_player == "1":
			mob_attack()
			user_attack()
		elif att_player == "2":
			print "Coming Soon"
		elif att_player == "3":
			print "Coming Soon"
		elif att_player == "4":
			print "You coward!!!"
			sys.exit()
	return True

mob = Mob(1, "Large Rat", 60, 60, 30)
print "You enter the dark cave then a %s goes to attack you" % mob.mob_name
win = False
while win == False:	
	win = battle()
print "You beat the %s and won the tresure" % mob.mob_name

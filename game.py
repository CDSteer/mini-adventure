import sys
import player
from player import * 
import mob
from mob import * 
import powers
from powers import *

"""runs the ballte options intill quit is selected or the mob or player is dead"""
def battle():
	while mob.is_alive() == True:
		print "%s, How will you attack?" % player.plr_name
		print "1. Basic Attack"
		print "2. %s Action Points: %r/%r" % (player.plr_power, player.plr_AP, player.plr_maxAP)
		print "3. Item"
		print "4. Quit"

		att_player = raw_input(">")
		
		if att_player == "1":
			mob_attack()
			user_attack()
		elif att_player == "2":
			if player.plr_AP >= power.power_cost: 
				player_power()
				mob_attack()
			else:
				print "Not Enough Action Points\n"
		elif att_player == "3":
			print "Coming Soon"
		elif att_player == "4":
			print "You coward!!!"
			sys.exit()
	return True

def user_attack():
	hp = mob.mob_HP
	dam = player.plr_att
	new_hp = hp - dam
	mob.mob_HP = new_hp
	print "You deal %r points of damage" % player.plr_att
	print "Level %r %s: %r/%r\n" % (mob.mob_lvl, mob.mob_name, mob.mob_HP, mob.mob_maxHP)
	if mob.poison:
		power.power_time + 1
		hp = mob.mob_HP
		dam = power.power_damage
		new_hp = hp - dam
		mob.mob_HP = new_hp
		print "%s is hurt by poison %r points of damage done" % (mob.mob_name, player.plr_att)
		print "Level %r %s: %r/%r\n" % (mob.mob_lvl, mob.mob_name, mob.mob_HP, mob.mob_maxHP)
		if power.power_time == 3:
			mob.poison = False
			power.power_time = 0
	return

def mob_attack():
	hp = player.plr_HP
	dam = mob.mob_att
	new_hp = hp - dam
	player.plr_HP = new_hp
	print "\n%s deals %r points of damage" % (mob.mob_name, mob.mob_att)
	if player.isalive(mob.mob_name) == False:
			sys.exit()
	print "Level %r %s: %r/%r\n" % (player.plr_lvl, player.plr_name, player.plr_HP, player.plr_maxHP)
	return
	
def player_power():
	if player.plr_class == "Rogue":
		mob.poison = True
	hp = mob.mob_HP
	dam = power.power_damage
	new_hp = hp - dam
	mob.mob_HP = new_hp
	print "%s deals %r points of damage" % (player.plr_power, dam)
	print "Level %r %s: %r/%r\n" % (mob.mob_lvl, mob.mob_name, mob.mob_HP, mob.mob_maxHP)
	cost = power.power_cost
	ap = player.plr_AP
	new_ap = ap - cost
	player.plr_AP = new_ap
	print "Level %r %s: Action Points: %r/%r\n" % (player.plr_lvl, player.plr_name, player.plr_AP, player.plr_maxAP)
	return

"""Game Starts here"""	
print "Welcome Player, start by entering your name:"
name = raw_input(">")
print "Hello there %s, \nYou are about to enter a cave of no return." % name
print "Once inside the only way back a mistic portal at the end." 
print "So why take this risk? Because within this cave lies the worlds" 
print "largest collection of tresuse hiden away by a long dead king and" 
print "protected by evil monsters, so good luck :D"

print "Choose you class:"
print "1. Warrior: Power = Rage"
print "2. Rogue:   Power = Poison"
print "3. Mage:    Power = Fireball"

plr_class = raw_input(">")
"""Set up the player depending on the class"""
if plr_class == "1":
	player = Player(1, name, "Warrior", "Rage", 300, 20, 30, 10)
	power = Rage(player.plr_att)
elif plr_class == "2":
	player = Player(1, name, "Rogue", "Poison", 200, 30, 20, 20)
	power = Poison(player.plr_att)
elif plr_class == "3":
	player = Player(1, name, "Mage", "Fireball", 100, 10, 10, 30)
	power = Fireball(player.plr_att)

print "Welcome %s the %s" % (player.plr_name, player.plr_class)

mob = Mob(1, "Large Rat", 60, 30, 10, 0)
print "You enter the dark cave then a %s goes to attack you:" % mob.mob_name
win = False
while win == False:	
	win = battle()
print "You beat the %s and won the tresure. Yay!" % mob.mob_name

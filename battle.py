import sys
import player
from player import * 
import mob
from mob import * 
import powers
from powers import *

player = Player()
mob = Mob()

def start_battle():
	mob.make_mob(player.plr_lvl)
	print "A wild %s appeared" % mob.mob_name
	return

def class_options(name):
	print "Choose you class:"
	print "1. Warrior: Power = Rage"
	print "2. Rogue:   Power = Poison"
	print "3. Mage:    Power = Fireball"

	plr_class = raw_input(">")
	"""Set up the player depending on the class"""
	if plr_class == "1":
		player.make_warrior(name)
	elif plr_class == "2":
		player.make_rogue(name)
	elif plr_class == "3":
		player.make_mage(name)
	return
 
def battle_options():

	print "How will you attack?"
	print "1. Basic Attack"
	player.print_AP()
	print "3. Item"
	print "4. Quit"
	att_player = raw_input(">")
	
	if att_player == "1":
		user_attack()
	elif att_player == "2":
		if mob.poison_check() == True:
			#Already poised 
			battle_options()
		elif mob.poison_check() == False: 
			player_power()		
	elif att_player == "3":
		print "Coming Soon"
		battle_options()
	elif att_player == "4":
		print "You coward!!!"
		sys.exit()	
	return True

def user_attack():
	dam = player.player_damage()
	dam = mob.mob_defence(dam)
	mob.damage_mob(dam)
	mob.print_HP()
	if mob.is_alive() == True:	
		if mob.poison == True:
			dam = player.poison_damage(mob.mob_name)
			mob.damage_mob(dam)
			mob.print_HP()
			mob_attack()
		else:
			mob_attack()
	else:
		player.xp_check(mob.mob_expValue)
		return

def mob_attack():
	dam = mob.mob_damage()
	dam = player.player_defence(dam)
	player.damage_player(dam, mob.mob_name)
	if player.isalive() == False:
		sys.exit()
	else:
		player.print_HP()
		battle_options()
	
def player_power():
	if player.AP_check() == True:
		player.cost_AP()
	else:
		battle_options()	
	if player.is_class("Rouge"):
		mob.poison = True
		print "%s has been poisoned" % mob.mob_name
		battle_options()
	else:
		dam = player.power_use()
		dam = mob.mob_defence(dam)
		mob.damage_mob(dam)
		mob.print_HP()
		player.print_AP2()
		if mob.is_alive() == True:
			mob_attack()
		else:
			player.xp_check(mob.mob_expValue)
			return
		
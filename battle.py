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
			battle_options()
		else: 
			player_power()		
	elif att_player == "3":
		bag_options()
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
		mob.get_item_drop(player.plr_lvl)
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
		mob.poison_mob()
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
			mob.get_item_drop(player.plr_lvl)
			return
			
def bag_options():
	player.open_battle_bag()
	selected_item = raw_input(">")
	if selected_item != "3":
		outcome = player.use_item(selected_item)
		if outcome == True:
			mob_attack()
		else:
			bag_options()
	else:
		battle_options()
	
	
	
	
	
	
	
	
	
	
	
	
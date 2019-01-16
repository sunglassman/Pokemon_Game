import time
import random

print('-' * 60)
print('A wild Jigglypuff appears!')
time.sleep(0.2)
print('You only have one Pokemon.')
time.sleep(0.2)
print('I choose you, Snorlax!!!!!!')
print()
time.sleep(0.2)

# Starting HPs
snorlax_hp = 200
jiggly_hp = 125

# Run Away Value

runaway_move = 5

# Print out the starting HP:
print('Original HP: ')
time.sleep(0.2)
print('- Snorlax HP: ' + str(snorlax_hp))
time.sleep(0.2)
print('- Jigglypuff HP: ' + str(jiggly_hp))
time.sleep(0.2)
print()
time.sleep(0.2)

while snorlax_hp > 0 and jiggly_hp > 0:
	print('Battle Options:')
	time.sleep(0.2)
	print('- [1] Sleep Heal')
	time.sleep(0.2)
	print('- [2] Tackle')
	time.sleep(0.2)
	print('- [3] Roundhouse Kick')
	time.sleep(0.2)
	print('- [4] Hyper Beam')
	time.sleep(0.2)
	print('- [5] Capture')
	time.sleep(0.2)
	print('- [6] Run Away')
	time.sleep(0.2)

	your_move = input('Choose a move using the corresponding number: ')
	print()
	if your_move == '1':
		snorlax_hp = snorlax_hp + 50
		print('Snorlax uses Sleep Heal, his HP increases to ' + str(snorlax_hp))
		time.sleep(0.2)
	elif your_move == '2':
		jiggly_hp = jiggly_hp - 10
		print('Snorlax uses tackle and deals 10 damage to Jigglypuff! ')
		time.sleep(0.2)
	elif your_move == '3':
		jiggly_hp == jiggly_hp - 30
		print('Snorlax uses roundhouse kick and deals 30 damage to Jigglypuff! ')
		time.sleep(0.2)
	elif your_move == '4':
		jiggly_hp = jiggly_hp - 40
		print('Snorlax uses hyperbeam and deals 40 damage to Jigglypuff!')
		time.sleep(0.2)
	elif your_move == '5':
		capture_roll = random.randint(0,125)
		if capture_roll > jiggly_hp:
			print('You have captured Jigglypuff! ')
			break
		else:
			print('You tried to capture Jigglypuff, but it escaped! ')
	elif your_move == '6':
		runaway_move = random.randint(1,10)
		if runaway_move > 5:
			print('You succesfully got away!')
			break
		else:
			print('You could not get away!')
		time.sleep(0.2)
	print()

	# jigglypuff attacks
	enemy_move = random.randint(1,2)
	enemy_move = str(enemy_move)

	if enemy_move == '1':
		snorlax_hp = snorlax_hp - 30
		jiggly_hp = jiggly_hp + 30
		print('Jigglypuff uses Drink Blood and deals 30 HP of damage while recovering 30 HP of health. ')
		time.sleep(0.2)
	elif enemy_move == '2':
		snorlax_hp = snorlax_hp - 50
		print('Jigglypuff uses Breathe Fire and deals 50 HP of damage. ')
		time.sleep(0.2)
	print()

	# Check for overkill and if so, set hp to 0
	if snorlax_hp < 0:
		snorlax_hp = 0
	if jiggly_hp < 0:
		jiggly_hp = 0

	print('Updated HP!')
	time.sleep(0.2)
	print('- Snorlax HP: ' + str(snorlax_hp))
	time.sleep(0.2)
	print('- Jigglypuff HP: ' + str(snorlax_hp))
	time.sleep(0.2)
	print()
	time.sleep(0.2)

if snorlax_hp == 0:
	print('Snorlax has been defeated! The winner is Jigglypuff! ')
elif jiggly_hp == 0: 
	print('Jigglypuff has been defeated! You are the winner! ')

print('You return to your base. ')
time.sleep(0.2)
print()

print('Your current HP is ' + str(snorlax_hp))

print('Options: ')
time.sleep(0.2)
print('- [1] Rest (Heal Up) ')
time.sleep(0.2)
print('- [2] Explore')
time.sleep(0.2)
print()

while snorlax_hp < 200:
	print()
	your_option = input('Choose an option: ')
	print()
	time.sleep(0.2)
	if your_option == '1':
		print('You rest at your base.')
		time.sleep(0.2)
		snorlax_hp = snorlax_hp + 100
		print('Your HP increases to ' + str(snorlax_hp))
		time.sleep(0.2)
	if snorlax_hp > 200:
		break
		

while snorlax_hp > 200:
		print()
		print('You return to the wild: ')
		time.sleep(2)
		print('Walking...')
		time.sleep(2)
		print('Walking...')
		time.sleep(2)
		break










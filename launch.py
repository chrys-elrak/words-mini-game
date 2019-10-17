#coding:utf-8
import random, os, sys
from functions import *

# 22740 words
"""
	* Author : Chrys Rakotonimanana
	* Date : Tue Oct 15 2019, 1:30 PM
	* Version : 1.0.0
	* Title : 22740 words
	* Description : Je me suis inspiré du jeux Word Charm, nottament sur mobile. Je voulais crée un jeux similaires, mais sur le terminal donc sans GUI.
"""


# variables
print(f"""{'*'*os.get_terminal_size().columns}
{' '*round(os.get_terminal_size().columns//2 - 6)}CHRYS RAKOTONIMANANA
{'*'*os.get_terminal_size().columns}
Entrer votre choix :
	1) Malagasy
	2) Français
""")
lang = ((input('>>> ')).strip()).lower()
if lang == '2':
	data = open_json('./mots.json')
else:
	data = open_json('./ohabolana.json')
player_name = ((input('Entrer votre nom : ')).lower()).strip()
continuer = None
score = get_score(player_name)

# main program
while True:

	x_word_list, x_word_str = choose_and_shuffle(data) # choose one and shuffle data
	res, text = find_like(str(x_word_list), data) # get all possible words with the main words choosen before
	# variables
	to_find, w_finded, b_finded, n = [], [], [], random.randrange(2, 5)

	# choose random words to find
	# all others will be a bonus  words
	while len(to_find) < n:
		random.shuffle(res)
		choosen = random.choice(res)
		if choosen not in to_find:
			to_find.append(choosen)
			res.remove(choosen)	

	#  while user doesn't find all words
	clear()
	while len(to_find) > 0:

		txt = ' · '.join(x_word_list)

		# -------------------------------------------------
		print('-' *  os.get_terminal_size().columns, end='')
		print(f"MOT MELANGER  : >>> {(txt).upper()} <<<")
		print(f'SCORE         : {score}')
		print(f'NOMBRE DE MOT A TROUVER : {len(to_find)}')
		if len(b_finded):
			print(f"BONUS TROUVER : {b_finded}")
		if len(w_finded):
			print(f"MOT TROUVER   : {w_finded}")
		print('-' *  os.get_terminal_size().columns, end='\n')
		# -------------------------------------------------

		print('Entrer le mot qui vous vient à l\'ésprit\nTapez :\n"." pour actualisez le mot\n"?" pour passer\n!" pour quitter')
		user_res = ((input('>>> ')).lower()).strip()
		clear()
		if user_res == '':
			print('Veuillez au moins entrer quelque chose !')
		# SHUFFLE
		elif user_res == '.':
			print('Acualisation ...')
			random.shuffle(x_word_list)
		# QUIT
		elif user_res == '!':
			print('Fermeture du programme ...')
			continuer = 'non'
			break
		# HELP 
		elif user_res == '?':
			if (score - 1 ) > 0:
				print('Vous ête perdu ?')
				show = random.choice(to_find)
				w_finded.append(show)
				to_find.remove(show)
				score -= 1
				print(f'VOILA : {show}')
			else:
				print('Désolé, Je ne peux pas vous aider, vous n\'avez pas assez de score :( ')
		# BONUS
		elif user_res in res and user_res not in to_find and user_res not in b_finded:
			b_finded.append(user_res)
			res.remove(user_res)
			score += .5
			print('BONUS')
		# TRUTH
		elif user_res in to_find and user_res not in w_finded:
			w_finded.append(user_res)
			to_find.remove(user_res)
			score += round(len(user_res) / 2)
			print('VRAIE')
		# WRONG
		else:
			if user_res in w_finded or user_res in b_finded:
				print('Déjà tapez')
			else:
				print('FAUX')
	if continuer == None:
		continuer = ((input('Voulez vous continuer ? (Oui / Non) : ')).lower()).strip()
		if continuer == 'non':
			break
		else:
			continuer = None
	else:
		break
print("""Choisiser une options :
	1 ) Quitter et Sauvegarder
	2 ) Quitter
	""")
o = ((input(">>> ")).lower()).strip()
if o == '1':
	set_score(score, player_name)
print('Fin de la partie, Au revoir !')
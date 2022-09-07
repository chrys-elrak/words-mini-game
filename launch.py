# coding:utf-8
import random
import os
import termcolor
from functions import *

# 22740 words
"""
	* Author : Chrys Rakotonimanana
	* Date : Tue Oct 15 2019, 1:30 PM
	* Version : 1.0.0
	* Title : 22740 words
	* Description : Je me suis inspiré du jeux Word Charm, nottament sur mobile. Je voulais crée un jeux similaires, mais sur le terminal donc sans GUI.
"""

data = get_lang()
player_name = input(termcolor.colored('Entrer votre nom: ', 'yellow')).lower().strip()
continuer = None
score = get_score(player_name)

# main program
while True:

    x_word_list, x_word_str = choose_and_shuffle(
        data)  # choose one and shuffle data
    # get all possible words with the main words choosen before
    res, text = find_like(str(x_word_list), data)
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
        print('-' * os.get_terminal_size().columns, end='')
        print(
            f"{termcolor.colored('MOT MELANGER', 'yellow', attrs=['underline'])}            : {termcolor.colored((txt).upper(), 'cyan',)}")
        print(
            f"{termcolor.colored('SCORE', 'yellow', attrs=['underline'])}                   : {score}")
        print(
            f"{termcolor.colored('NOMBRE DE MOT A TROUVER', 'yellow', attrs=['underline'])} : {len(to_find)}")
        if len(b_finded):
            print(
                f"{termcolor.colored('BONUS TROUVER', 'yellow', attrs=['underline'])} : {b_finded}")
        if len(w_finded):
            print(
                f"{termcolor.colored('MOT TROUVER', 'yellow', attrs=['underline'])}   : {termcolor.colored(w_finded, attrs=['bold'])}")
        print('-' * os.get_terminal_size().columns, end='\n')
        # -------------------------------------------------

        print(
            f'''Entrer le mot qui vous vient à l'ésprit, Tapez :\n{termcolor.colored("*", 'red')} pour actualiser\n{termcolor.colored("?", 'yellow')} pour passer\n{termcolor.colored("!", 'green')} pour quitter'''
        )
        user_res = ((input('> ')).lower()).strip()
        clear()
        if user_res == '':
            print('Veuillez au moins entrer quelque chose !')
        # SHUFFLE
        elif user_res == '*':
            print(termcolor.colored('Acualisation ...', 'cyan'))
            random.shuffle(x_word_list)
        # QUIT
        elif user_res == '!':
            print('Fermeture du programme ...')
            continuer = 'non'
            break
        # HELP
        elif user_res == '?':
            if (score - 1) > 0:
                print(f'{termcolor.colored("?", "yellow")} Vous ête perdu')
                show = random.choice(to_find)
                w_finded.append(show)
                to_find.remove(show)
                score -= 1
                print(f"VOILA : {termcolor.colored(show, attrs=['bold'])}")
            else:
                print(
                    'Désolé, Je ne peux pas vous aider, vous n\'avez pas assez de score :( ')
        # BONUS
        elif user_res in res and user_res not in to_find and user_res not in b_finded:
            b_finded.append(user_res)
            res.remove(user_res)
            score += .5
            print(termcolor.colored('BONUS', 'green'))
        # TRUTH
        elif user_res in to_find and user_res not in w_finded:
            w_finded.append(user_res)
            to_find.remove(user_res)
            score += round(len(user_res) / 2)
            print(termcolor.colored('VRAIE', 'green'))
        # WRONG
        else:
            if user_res in w_finded or user_res in b_finded:
                print(termcolor.colored('Déjà tapez', 'magenta'))
            else:
                print(termcolor.colored('FAUX', 'red'))
    if continuer is None:
        continuer = input(
            'Voulez vous continuer ? (Oui / Non) : ').lower().strip()
        if continuer == 'non':
            break
        else:
            continuer = None
    else:
        break

save_prompt(score, player_name)

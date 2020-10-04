import csv
import json
import os
import random
import sys


def open_json(file):
	with open(file, encoding='utf-8') as json_file:
		json_data = json.load(json_file)
	return json_data


def write_json(file):
	with open(file, mode='w') as json_file:
		json_file.write(json.dumps(file, sort_keys=True, indent=4))


def choose_and_shuffle(data):
	x_word_str = random.choice(data)
	x_word_list = list(x_word_str)
	random.shuffle(x_word_list)
	return x_word_list, x_word_str


def find_like(text, mots):
	text = text.lower()
	res = []
	for mot in mots:
		mot = mot.lower()
		_tmp = {}
		for char in mot:
			if char in text:
				if _tmp.get(mot) is None:
					_tmp[mot] = []
					_tmp[mot].append(char)
				else:
					if char not in _tmp[mot] or text.count(char) >= mot.count(char):
						_tmp[mot].append(char)
					if len(mot) == len(_tmp[mot]) and mot != text:
						res.append(mot)
	return res, text


def set_score(score, player_name):
	data = []

	with open('score.csv', mode='r') as score_file_r:

		reader = csv.reader(score_file_r, delimiter=',', quotechar='|')

		for row in reader:
			data.append(row) # storing data as list

		try:
			p = [(k, v)for k, v in enumerate(data) if player_name in v][0]
		except IndexError:
			p = None
		finally:
			if p:
				# update the score for the user
				data[p[0]][-1] = float(score)

				with open('score.csv', mode='w', newline='\n') as score_file_w:
					writer = csv.writer(score_file_w, delimiter=',', quotechar='|')
					for d in data:
						writer.writerow(d)
			else:
				# add new user with his score
				with open('score.csv', mode='a', newline='\n') as score_file_a:
					writer = csv.writer(score_file_a, delimiter=',', quotechar='|')
					writer.writerow([player_name, score])


def get_score(player_name):
	data = []
	with open('score.csv') as score_file_r:
		reader = csv.reader(score_file_r, delimiter=',', quotechar='|')
		for row in reader:
			data.append(row)
		try:
			p = [(k, v)for k, v in enumerate(data) if player_name in v][0]
		except IndexError:
			p = None
		finally:
			if p:
				return float(data[p[0]][-1])
			else:
				return 0


def clear():
	if sys.platform == "linux":
		os.system('clear')
	elif sys.platform == "win32":
		os.system('cls')


if __name__ == "__main__":
	print("You can not execute this file")

# -*- coding:utf-8 -*-
import json

with open('ohabolana.txt', encoding='utf-8') as file:
	words_list = file.read().split()
	words_list.sort()
words = []

for word in words_list:
	word = (word.strip('\ufeff.():;,“"-«»…!0123456789:*=<>')).lower()
	if word not in words and len(word) > 1:
		words.append(word)
words.sort()
with open('ohabolana.json', mode='w') as json_file:
	json_file.write(json.dumps(words, sort_keys=True, indent=4, ensure_ascii=False))
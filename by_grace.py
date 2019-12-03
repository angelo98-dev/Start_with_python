#-*-coding : utf8 -*-
from random import randint

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]

def get_random_item(my_list):
	rand_num = randint(0,len(my_list) - 1)
	item = my_list[rand_num]
	return item

def message(character, quote):
	character = character.capitalize()
	quote = quote.capitalize()
	return "{} says : {}".format(character, quote)



user_answer = input("Type Enter for an other quote or Q (q) to quit : ")
while (user_answer != "Q"):
	print(message(get_random_item(characters), get_random_item(quotes)))
	user_answer = input("Type Enter for an other quote or B to quit : ")
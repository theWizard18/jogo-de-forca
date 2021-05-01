import random
import os
from hangman_visual import hangman_visual_dict

def make_word():
	try:
		with open('./words.txt') as f:
			words = f.read().splitlines()
		word = random.choice(words)
		return word
	except:
		print('Não foi possivel encontrar o arquivo \'words.txt\'')
		return -1
	


def make_remaining_letters(word):
	remaining_letters = []
	for letter in word:
		if letter in remaining_letters:
			continue
		else:
			remaining_letters.append(letter)
	return remaining_letters


def get_guess(guesses):
	while True:
		guess = input('insira uma letra: ')
		guess = guess.lower()
		if len(guess) != 1:
			print('você deve entrar uma letra')
		elif guess in guesses:
			print('você já entrou essa letra')
		else:
			guesses.append(guess)
			return guess


def print_word(word, guess, remaining_letters):	
	print(end='   \"')
	for letter in word:
		if guess == letter or letter not in remaining_letters:
			print(end=letter)
		else:
			print(end='_')
	print('\"\n')


def check_strikes(word, guess, remaining_letters):
	for letter in word:
		if guess == letter:
			remaining_letters.remove(guess)
			return True
	return False


def game():
	os.system('clear')
	word = make_word()
	if word == -1:
		return word
	
	remaining_letters = make_remaining_letters(word)
	guesses = []
	lives = 7
	guess = ""
	while True:
		strike = False
		os.system('clear')
		
		print('tentativas:', guesses)
		
		strike = check_strikes(word, guess, remaining_letters)
		if strike == False:
			lives -= 1
		
		print(end=hangman_visual_dict[lives])
		print_word(word, guess, remaining_letters)
		if len(remaining_letters) == 0 or lives == 0:
			break
		
		guess= get_guess(guesses)
	
	if len(remaining_letters) == 0:
		print('você ganhou')
	else:
		print('você perdeu')
		print('a palavra era', word)


game()

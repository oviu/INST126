"""Hangman Text Game

A basic text-based implementation of the game Hangman. Users,
have 10 lives to guess all the correct letters of a random
encrpyted word. They are not penalized a life if they guess a
correct letter, if they use a used letter, or enter something other
than a letter. If they win, the encrypted word is decrypted and
revealed to them.
"""

from random import randint

'''Given the encryption flowchart, the reverse decrypt function
   is simply subtracting each character ASCII by 1 if even
   or add 1 if odd, instead of adding 1 if even and subtracting 1 if odd.'''
def decrypt(ciphertext):
	"""Returns the plaintext from the ciphertext"""
	plaintext = ""
	i = 0
	while i < len(ciphertext):
		if(i % 2 == 0):
			cipher_ascii = ord(ciphertext[i])
			plain_ascii = cipher_ascii - 1
		else:
			cipher_ascii = ord(ciphertext[i])
			plain_ascii = cipher_ascii + 1
		plaintext += chr(plain_ascii)
		i += 1
	return plaintext

words = ["WHDSPQZ", "XHO", "TTDBFRT", "QQJYF", "ENQD", "DNPK", "CNTR", "EHWHOD", "TSVMOHOF", "XNOCFQGTM"]

game_word = words[randint(0,9)]
hidden_word = len(game_word) * "_"
letters_used = set()
guess_count = 0
guess = None

while guess_count < 10:
	print(f"you have {10 - guess_count} lives left and have used these letters: {''.join(letters_used)}")
	print(f"current word {hidden_word}")

	guess = input("Guess a letter: ").upper()

	#guess should only be a letter and not have been used, anything else redirects to another attempt
	if guess in letters_used or not guess.isalpha() or len(guess) > 1:
		print("oops! letter is already in use or invalid guess.")
		continue
	else:
		letters_used.add(guess)

	guess_indices = [i for i, letter in enumerate(game_word) if letter == guess]

	#if guess_indices is empty that means the guess letter was not found in the word
	if not guess_indices:
		guess_count += 1
		if guess_count == 10:
			print("sorry, you lost")
		continue
	
	# If guess_indices is not empty, we replace hidden_word '_' characters with guess letter at their respective
	# indices. Lists are mutable so converting string to list to replace indexes then back to string for ease
	else:
		hidden_word = list(hidden_word)
		for i in guess_indices:
			hidden_word[i] = guess
		hidden_word = "".join(hidden_word)

	if hidden_word == game_word:
		print(hidden_word)
		print("you win!")
		print(f"The decrypted word is {decrypt(hidden_word)}")
		break






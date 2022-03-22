#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from passlib.hash import bcrypt
from libs import pingo
from colored import fg
import sys



def tryCrack(hash, words):
    print(blueColor)
    for (index, word) in enumerate(words):
        pingo(index + 1, length, prefix=blueColor + 'Wait:', suffix='')
        correct = bcrypt.verify(word, hash)
        if (correct):
            correct_word = word
            return correct_word
    return ''


greenColor = fg('#008000')
redColor = fg('#800000')
blueColor = fg('#0022ff')

print(blueColor + "\n*************************************************")
print(blueColor + "Debcrypt - Password cracker tools for bcrypt hash")
print(blueColor + "*************************************************")
options = input(blueColor + '\nYou want to crack? y/n: ')

if (options == "n"):
    sys.exit()
elif (options != "y" and options != "n"):
    sys.exit(redColor + 'Invalid Option')

passwords = (options == "y")
words_text_file = open("words.txt", "r", encoding="cp437")
hashes_text_file = open("hashes.txt", "r", encoding="cp437")

words = words_text_file.read().splitlines()


length = len(words)

hashes = hashes_text_file.read().splitlines()

for (index, hash) in enumerate(hashes):
    cracked = tryCrack(hash, words)
    if (cracked):
        print(greenColor + "\n\n#" + str(index + 1) + " Password found:", cracked)
    else:
        print(redColor + "\n\n#" + str(index + 1) + " Unfortunately, password not found.")

print(blueColor + "\n\nDone.")
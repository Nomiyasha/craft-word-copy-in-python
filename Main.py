import Downloader
import Round
# URL: "https://drive.google.com/uc?id=0B5eYVI2s0XztOVdaUnNWQWFZOEU"
# ZIP: "words.zip"
# OUT: "words"

# Program entry point for a craft word copy
# :)
# This code is very uncommented.
# Shoutout to Ashley Bovan for her word list which I use here

all_words = Downloader.AllWords().words
valid_words = Downloader.AllWords().valid_words


print("""In this game, the goal is to get from one word to another.
Each step on the way is counted towards your score, and the lower the score the better!
Valid moves are:
    Remove a character from a word
    Add a character to a word
    Rearrange all characters in a word
    Replace a character in a word
Naturally, all words must be correct english!""")

score = Round.game(all_words, valid_words)

print(f"Score: {score}")

while True:
    choice = input("Would you like to play again? (y/n): ")
    if choice != 'y':
        print("Thanks for playing!")
        break

    score = Round.game(all_words, valid_words)

    print(f"Score: {score}")











import Turn
import random

# Plays the game and runs the turn object against the words provided from downloader
# Returns the amount of moves taken to get to the goal word
def game(all_words, valid_words) -> int:
    random.seed()

    word = valid_words[random.randrange(len(valid_words))]
    goal = valid_words[random.randrange(len(valid_words))]
    print(f"Your goal is {goal}. Good luck!")
    moves = 1
    this_turn = Turn.Turn(word, all_words, goal)

    while True:
        if this_turn.new_word == goal:
            return moves
        moves += 1
        this_turn = Turn.Turn(this_turn.new_word, all_words, goal)

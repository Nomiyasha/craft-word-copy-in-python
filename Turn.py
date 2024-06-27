# Contains the class turn, which compares a given word to a word entered by the player
class Turn:
    def __init__(self, word, dictionary, goal):
        self.word = word.lower()
        self.dictionary = dictionary
        self.goal = goal.lower()
        try:
            while True:
                self.new_word = input(f"Your word is {self.word.upper()}, the goal is {self.goal.upper()}. Enter a new word: ").lower()
                if self.__final_check():
                    break

        except TypeError:
            print("You must enter a word")

    # Checks the new word against the dictionary and checks if it is a valid move
    def __final_check(self) -> bool:
        if not self.__spell_check():
            print("Not in dictionary!")
            return False
        if not self.__move_check():
            print("Invalid move.")
            return False
        return True

    # Checks so that the user entered word is in the dictionary
    def __spell_check(self) -> bool:
        if self.new_word not in self.dictionary:
            return False
        return True

    # Checks so that the user entered word is a valid move according to the rules
    def __move_check(self) -> bool:
        try:
            if self.__add() or self.__remove() or self.__rearrange() or self.__replace():
                return True

        except ValueError:
            print("Invalid input.")
            self.new_word = input("Enter: ").lower()

    # Checks if one character has been added.
    def __add(self) -> bool:
        if self.word == self.new_word or len(self.word) + 1 != len(self.new_word):
            return False

        if self.__difference_counter() != 1:
            return False
        return True

    # Checks if one character has been removed.
    def __remove(self) -> bool:
        if self.word == self.new_word or len(self.word) - 1 != len(self.new_word):
            return False

        if self.__difference_counter() != 1:
            return False
        return True

    # Checks if the word has been rearranged, ie if the two words, the old and the newly entered one, are anagrams
    def __rearrange(self) -> bool:

        if len(self.word) != len(self.new_word) or self.word == self.new_word:

            return False
        if self.__difference_counter() != 0:
            return False
        return True

    # Checks if one character has been replaced. Essentially checks if the words are anagrams one character off.
    def __replace(self) -> bool:

        if len(self.word) != len(self.new_word) or self.word == self.new_word:
            return False

        if self.__difference_counter() != 1:
            return False
        return True

    # A function that returns the amount of difference found in two strings
    # It does so by first making sure that the strings are of equal length
    # Then it goes through the strings and counts each difference
    # Then it returns the differences divided by 2 since the differences will be recorded twice
    def __difference_counter(self) -> int:
        temp_word = self.word
        temp_new_word = self.new_word

        # we are in remove
        if self.word > self.new_word:
            temp_word = self.word
            for i in range(len(self.word)-len(self.new_word)):
                temp_new_word = self.new_word + " "
        # we are in add
        elif self.word < self.new_word:
            temp_new_word = self.new_word
            for i in range(len(self.new_word)-len(self.word)):
                temp_word = self.word + " "


        counts = {}
        errors = 0

        for c1, c2 in zip(temp_word, temp_new_word):
            if c1 in counts:
                counts[c1] += 1
            else:
                counts[c1] = 1
            if c2 in counts:
                counts[c2] -= 1
            else:
                counts[c2] = -1

        for count in counts.values():
            if count != 0:
                errors += 1
        #print(f"{errors} errors, {temp_word}, {temp_new_word}.")
        if errors == 1:
            return errors
        return int(errors/2)


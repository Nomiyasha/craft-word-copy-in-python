# create something that compares two words and sees if it is a legal move between them
# legal moves: add, remove, change, rearrange



class Turn:
    def __init__(self, word, dictionary):
        self.word = word.lower()
        self.dictionary = dictionary

        try:
            while True:
                self.new_word = input(f"The your word is {word}. Enter a new word: ").lower()

                if self.__move_check() and self.__spell_check():
                    break
                else:

                    print("Invalid move.")
        except TypeError:
            print("You must enter a word")

    def __spell_check(self):
        if self.new_word not in self.dictionary:
            return False
        return True

    def __add(self):

        if self.word == self.new_word or len(self.word) + 1 != len(self.new_word):
            return False
        temp_word = self.word + " "

        if self.__difference_counter(temp_word) != 1:
            return False
        #print("pass add")
        return True

    def __remove(self) -> bool:
        if self.word == self.new_word or len(self.word)-1 != len(self.new_word):
            return False

        temp_new_word = self.new_word + " "

        if self.__difference_counter(self.word, temp_new_word) != 1:
            return False

        #print("pass remove")
        return True

    def __rearrange(self) -> bool:

        if len(self.word) != len(self.new_word) or self.word == self.new_word:

            return False
        counts = {}

        for c1, c2 in zip(self.word, self.new_word):
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
                return False
        #print("pass rearr")
        return True

    def __replace(self) -> bool:

        if len(self.word) != len(self.new_word) or self.word == self.new_word:
            return False

        if self.__difference_counter() != 1:

            return False
        #print("pass replace")
        return True

    def __move_check(self) -> bool:
        try:
            if self.__add() or self.__remove() or self.__rearrange() or self.__replace():
                return True

        except ValueError:
            print("Invalid input. 1")
            self.new_word = input("Enter: ").lower()

    def __difference_counter(self, word="", new_word="") -> int:
        if word == "":
            word = self.word
        if new_word == "":
            new_word = self.new_word
        count = 0
        for ch in range(len(word)):
            if word[ch] != new_word[ch]:
                count += 1
        return count

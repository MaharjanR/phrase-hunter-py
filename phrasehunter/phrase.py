from phrasehunter.character import Character

# Create your Phrase class logic here.

class Phrase():
    def __init__(self, phrase, words_left = 0):
        self.phrase = [Character(char) for char in phrase]
        self.words_left = words_left
        print(self.phrase)
        

    def display_phrase(self):
        self.words_left = 0
        for char in self.phrase:
            print(char.display(), end=" ")
            if char.display() == '_':
                self.words_left += 1
        
        if self.words_left == 0:
            return True
        else:
            return False

    def guess(self, guess_char):
        guessed = False
        for char in self.phrase:
            char.guess(guess_char)
            if char.guess(guess_char) == True:
                guessed = True
        return guessed
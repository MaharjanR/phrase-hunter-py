# Create your Character class logic in here.

class Character():
    def __init__(self, char, was_guessed = False):
        self.char = char
        self.was_guessed = was_guessed

    def guess(self, guess):
        if self.char.lower() == guess:
            self.was_guessed = True
            return True

    def display(self):
        if self.char == ' ':
            return self.char
        elif self.was_guessed:
            return self.char
        else:
            return '_'
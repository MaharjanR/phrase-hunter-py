import random
from phrasehunter.phrase import Phrase

# Create your Game class logic in here.

class Game():
    def __init__(self, phrases, life = 5):
        self.phrases = phrases
        self.current_phrase = ''
        self.life = life

    def set_active_phrase(self):
        random_num = random.randint(0, ( len(self.phrases) - 1) )
        self.current_phrase = Phrase(self.phrases[random_num])

    def game_over(self, text):
        print("\n=======================================")
        print(text)
        print("=======================================")
        user_input = input("Do you still want to play the game? (y/n): ")
        if user_input == 'y':
            self.life = 5
            self.start_game()
        else:
            print("Sad to see you go :(")

    def start_game(self):
        self.set_active_phrase()
        game_won = False

        print("Welcome to Phrase Hunter\n")
        while not game_won:
            print(f'\nTotal Lives left: {self.life}')
            game_won = self.current_phrase.display_phrase()
            if not game_won:
                user_input = input("\n\nPlease enter a letter: ").lower()
                while len(user_input) > 1 or not user_input.isalpha():
                    print("Please enter one letter only. Thank you!!")
                    user_input = input("\n\nPlease enter a new letter: ").lower()
                guessed = self.current_phrase.guess(user_input)
                if guessed == False:
                    self.life -= 1
                    if self.life == 0:
                        self.game_over("Sorry, you lost the game")
                        break
            else:
                self.game_over("Congratulation, you won the game")
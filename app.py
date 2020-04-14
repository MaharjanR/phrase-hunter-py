# Import your Game class
from phrasehunter import game

phrases = ['My name is', 'python', 'JavaScript']
# Create your Dunder Main statement.
# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
if __name__ == "__main__":
    game1 = game.Game(phrases)
    game1.start_game()
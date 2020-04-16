# Importing Game class
from phrasehunter import game

# Phrases for the game
phrases = ['I love Python', 'Everything is fair in Love and War', 'I am awesome']

# calls the game class
if __name__ == "__main__":
    game1 = game.Game(phrases)
    game1.start_game()
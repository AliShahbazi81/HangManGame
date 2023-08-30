import random


class HangmanGame:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word_to_guess = random.choice(self.word_list).upper()
        self.display_word = ['_'] * len(self.word_to_guess)
        self.incorrect_guesses = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

    def display(self):
        print(" ".join(self.display_word))
        print(f"Incorrect Guesses: {', '.join(self.incorrect_guesses)}")
        print(f"Attempts Left: {self.attempts_left}")

    def make_guess(self, guess):
        guess = guess.upper()
        if len(guess) != 1:
            print("Please guess one letter at a time.")
            return

        if guess in self.display_word or guess in self.incorrect_guesses:
            print("You've already guessed that letter.")
            return

        if guess in self.word_to_guess:
            for index, letter in enumerate(self.word_to_guess):
                if letter == guess:
                    self.display_word[index] = guess
        else:
            self.incorrect_guesses.append(guess)
            self.attempts_left -= 1

    def is_winner(self):
        return '_' not in self.display_word

    def is_loser(self):
        return self.attempts_left <= 0

    def play(self):
        print("Welcome to Hangman!")
        while not self.is_winner() and not self.is_loser():
            self.display()
            guess = input("Guess a letter: ")
            self.make_guess(guess)

        self.display()
        if self.is_winner():
            print("Congratulations! You've won!")
        else:
            print(f"Sorry, you've lost. The word was: {self.word_to_guess}")


# Sample word list for the game
word_list = ["python", "hangman", "programming", "developer"]

game = HangmanGame(word_list)
game.play()

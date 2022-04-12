import random
from colorama import init, Back
from english_words import english_words_alpha_set

words = [word.upper() for word in english_words_alpha_set if len(word) == 5]
init(autoreset=True)

class Wordle:

    def __init__(self):
        self.tries = 0
        self.board = ['_____'] * 6
        self.answer = random.choice(words)
        self.alphabet = {char : Back.RESET for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
        self.output_board()
        self.run_game()

    def run_game(self):
        while self.tries < 6:
            self.make_guess()
            print(chr(27) + "[2J")
            self.output_board()
        print('Sorry, try again!\nThe word was ' + self.answer)
        exit(0)
    
    def output_board(self):
        for line in self.board:
            print(line)
        for key in self.alphabet:
            print(self.alphabet[key] + key, end = '')
        print()

    def make_guess(self):
        guess = input('Make a guess: ').upper()
        guess_cpy = guess
        if guess not in words:
            print(guess + ' is not a valid 5-letter word.')
            return
        # elif guess == self.answer:
        #     guess = Back.GREEN + guess
        #     self.board[self.tries] = guess
        #     print(chr(27) + "[2J")
        #     self.output_board()
        #     print('Correct, congratulations!')
        #     exit(0)
        already_used = []
        for guess_char, answer_char in zip(guess, self.answer):
            if guess_char == answer_char:
                guess = guess.replace(guess_char, Back.GREEN + guess_char, 1)
                self.alphabet[guess_char] = Back.GREEN # self.alphabet.replace(guess_char, Back.GREEN + guess_char, 1)
            elif guess_char in self.answer:
                guess = guess.replace(guess_char, Back.YELLOW + guess_char, 1)
                self.alphabet[guess_char] = Back.YELLOW #= self.alphabet.replace(guess_char, Back.YELLOW + guess_char, 1)
            else:
                if guess_char in already_used:
                    continue
                already_used.append(guess_char)
                guess = guess.replace(guess_char, Back.RESET + guess_char, 2)
                self.alphabet.pop(guess_char, 'No value')
        if guess_cpy == self.answer:
            guess = Back.GREEN + guess
            self.board[self.tries] = guess
            print(chr(27) + "[2J")
            self.output_board()
            print('Correct, congratulations!')
            exit(0)
        self.board[self.tries] = guess
        self.tries += 1
        

def main():
    wordle = Wordle()

main()
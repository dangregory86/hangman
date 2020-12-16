import random

words = ['banana', 'fruit', 'car']
blank_word = []
guessed_letters = []
word_to_guess = words[random.randint(0, 2)]
lives = [9]
blank = ' - '
won = [False]

# TODO make it into a single function that starts and runs a full game.

for i in word_to_guess:
    blank_word.append(blank)
print(blank_word)


def letters_left_to_guess():
    if blank not in blank_word:
        won[0] = True

def remove_life():
    lives[0] -= 1
    print('That letter is not in the word\nYou now have ' + str(lives[0]) + ' remaining!')
    
# check if a letter has been used before
def letter_used_before(letter):
    x = 0
    if len(guessed_letters) > 0:
        while x < len(guessed_letters):
            if letter == guessed_letters[x]:
                return True
    return False

def check_letter(letter):
    count = 0
    num_letters = 0
    guessed_letters.append(letter)
    while count < len(word_to_guess):
        if letter == word_to_guess[count]:
            blank_word[count] = letter
            num_letters += 1
        count += 1
    if num_letters == 0:
        remove_life()
    print('letters you have guessed: ', guessed_letters)
    print(blank_word)
    

moves = 0
while True:
    line = input('Enter a letter to guess: ')
    if line == 'quit':
        break
    check_letter(line)
    letters_left_to_guess()
    moves += 1
    if won[0]:
        print('you won!! in ' + str(moves) + ' moves!')
        break
    if lives[0] < 1:
        print('Game over loser!!')
        break
    
print('done')
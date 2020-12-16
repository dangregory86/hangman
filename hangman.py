import random

file = open('word_list.txt', 'r')
content = file.read()
file.close()
words = content.split()
blank_word = []
guessed_letters = []
word_to_guess = words[random.randint(0, len(words) - 1)]
lives = [7]
blank = '*'
won = [False]



for i in word_to_guess:
    blank_word.append(blank)
print(''.join(blank_word))


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
    print(''.join(blank_word))
    
while True:
    line = input('Please enter your next guess:')
    if line == 'quit':
        break
    check_letter(line)
    letters_left_to_guess()
    if won[0]:
        print('congratulations you win')
        break
    if lives[0] < 1:
        print('you lose')
        break

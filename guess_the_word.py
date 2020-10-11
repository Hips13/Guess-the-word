import random

print('H A N G M A N')


def menu():
    print()
    while True:
        option = input('Type "play" to play the game, "exit" to quit:')
        if option == 'play':
            game()
        elif option == 'exit':
            break
        else:
            break


def game():
    print()
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)
    hyphens = ['-'] * len(word)
    print(''.join(hyphens))

    en_words = 'abcdefghijklmnopqrstuvwxyz'
    stack_letter = []
    try_ = 1
    while True:
        letter = input('Input a letter: ')
        if len(letter) != 1:
            print('You should input a single letter')
            print()
            print(''.join(hyphens))
            continue
        if letter not in en_words:
            print("It is not an ASCII lowercase letter")
            print()
            print(''.join(hyphens))
            continue
        if letter not in word:
            if letter in stack_letter:
                print("You already typed this letter")
                print()
                print(''.join(hyphens))
            else:
                print("No such letter in the word")
                print()
                print(''.join(hyphens))
                try_ += 1
                if try_ >= 8:
                    print("No such letter in the word")
                    print('You lost!')
                    break
        if letter in word:
            if letter in stack_letter:
                print("You already typed this letter")
            for i in range(len(word)):
                if word[i] == letter:
                    hyphens[i] = word[i]
            print()
            print(''.join(hyphens))
        if ('-' not in hyphens) and (try_ < 8):
            print(f"You guessed the word {''.join(hyphens)}")
            print("You survived!")
            break
        stack_letter += letter


menu()


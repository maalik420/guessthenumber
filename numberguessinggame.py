import art
import random

def check_the_guess_number(guess_by_player, guessed_by_host,):
    if guess_by_player == guessed_by_host:
        return 'You got it!!'
    elif guess_by_player < guessed_by_host:
        return 'No, this number is too low'
    else:
        return 'No, this number is too high'

def guessing_game(no_of_guesses,):
    answer = ''
    while no_of_guesses > 0 and answer != 'You got it!!':
        guess_by_player = int(input('Now tell me what number I guessed  between 1 and 100'))
        if guess_by_player < 1 or guess_by_player > 100:
            print('Sorry, but you have guessed the invalid number')
            break
        answer = check_the_guess_number(guess_by_player, guessed_by_host,)
        print(answer)
        print(f'You have {no_of_guesses - 1} guesses left')
        no_of_guesses -= 1
    if no_of_guesses == 0 and answer != 'You got it!!':
        print(f'Boom!!! Your attempts are over and the number was {guessed_by_host}')

print(art.logo)
print('Welcome to the number guessing game!!')
guessed_by_host = random.randrange(1, 100)
print('I have guessed the number between 1 and 100. Let\'s play guessing...')
choice = input('Choose difficulty level: easy or hard')

if choice.lower() == 'easy':
    no_of_guesses = 10
    guessing_game(no_of_guesses)
else:
    no_of_guesses = 5
    guessing_game(no_of_guesses)

from num2words import num2words
import random

liner = ('____________________')
the_answer = random.randint(0, 9)
total_guess = random.randint(3, 4)
i = 0
print('\nWelcome to Can.You.Guess.The.Number!?')
print(f'You have {num2words(total_guess)} guesses.')
print('The answer is one digit.\n')
print(liner)

while i < total_guess:
    try:
        guess = int(input('Please guess the number.\n'
                          'Here: '))
        if guess == the_answer:
            print(f'Well played: {the_answer} is the answer. 👌')
            print('You won')
            print(liner)
            break
        else:
            i += 1
            guess_left = total_guess - i
            if guess_left > 0:
                print('Nope! Sorry. 😊')
                print(f'You have {guess_left} more guess{'es' if guess_left > 1 else ''}.')
                print(liner)

            else:
                print('Game is over.')
                print(f'The correct answer was {the_answer}.')
                print(liner)
    except ValueError:
        print('Please enter a valid number.')
        print(liner)





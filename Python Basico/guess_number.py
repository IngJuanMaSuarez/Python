import random


def run():
    gues_number = random.randint(1, 100)
    user_number = int(input('Enter a number from 1 to 100 '))
    while user_number != gues_number:
        if user_number < gues_number:
            print('Please enter a larger number')
        else:
            print('Please enter a smaller number')
        user_number = int(input('Enter a number from 1 to 100 '))
    print('¡You win!')


if __name__ == '__main__':
    run()
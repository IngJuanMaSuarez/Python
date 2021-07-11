def is_prime(number):
    counter = 0

    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            counter += 1
            break
    if counter == 0:
        return True
    else:
        return False


def run():
    number = int(input('Enter a number: '))
    if is_prime(number):
        print('Its prime')
    else:
        print('Its not prime')


if __name__ == '__main__':
    run()
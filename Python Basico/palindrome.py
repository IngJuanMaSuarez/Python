def palindrome(phrase):
    phrase = phrase.replace(' ', '').lower()
    inverted_phrase = phrase[::-1]
    if phrase == inverted_phrase:
        return True
    else:
        return False


def run():
    phrase = input('Enter a phrase: ')
    is_palindrome = palindrome(phrase)
    if is_palindrome == True:
        print('Its palindrome')
    else:
        print('Its not palindrome')


if __name__ == '__main__':
    run()
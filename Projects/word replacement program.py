from codecs import replace_errors


def replace_word():
    str = "Hi guys I'm Patryk"
    word_to_replace = input('Enter the word to replace: ')
    word_replacement = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word_replacement))


replace_word()
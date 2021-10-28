import string
import random


def generate_grid() -> list[list[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    alphabet = string.ascii_uppercase
    letters_grid = [
        [alphabet[random.randint(0, 25)] for _ in range(3)] for _ in range(3)
    ]
    #check whether 5 different letters appear in grid
    unique = ''
    for row in range(3):
        for col in range(3):
            if letters_grid[row][col] not in unique:
                unique+=letters_grid[row][col]
    if len(unique)<5:
        letters_grid = generate_grid()
    
    return letters_grid


def count_appearances(word: str) -> list[tuple]:
    counter_letter = []
    for i in range(len(word)):
        if i == 0:
            counter_letter.append((word[i], word.count(word[i])))
        elif word[i] not in word[:i] and i != 0:
            counter_letter.append((word[i], word.count(word[i])))
    return counter_letter


def check_rules(letters:list[str],word):
    correct = False
    if len(word) >= 4 and letters[4] in word.lower():
                correct = True
                count_word = count_appearances(word.lower())
                for appearance in count_word:
                    if appearance[0] not in letters or appearance[1] > letters.count(
                        appearance[0]):
                        correct = False
                        break
    return correct


def get_words(f: str, letters: list[str]) -> list[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    legal_words = []
    with open(f, "r") as dictionary:
        for word in dictionary.readlines():
            if check_rules(letters,word[:-1]) and word[:-1].lower() not in legal_words:
                legal_words.append(word[:-1].lower())
    return legal_words


def get_user_words() -> list[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    user_words = []
    word = 'hi'
    print("Try to find some words)")
    while word != '':
        word = input()
        user_words.append(word)
    return user_words[:-1]


def get_pure_user_words(
    user_words: list[str], letters: list[str], words_from_dict: list[str]
) -> list[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pure_user_words = []
    for word in user_words:
        if check_rules(letters,word) and word not in words_from_dict:
            pure_user_words.append(word)
    return pure_user_words
    


def results():
    pass


if __name__ == "__main__":
    # print(get_words("en", ["e", "t", "x", "p", "h", "z", "o", "l", "i"]))
    # print(get_user_words())
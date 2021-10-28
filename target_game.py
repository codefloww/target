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
    return letters_grid


def count_appearances(word: str) -> list[tuple]:
    counter_letter = []
    for i in range(len(word)):
        if i == 0:
            counter_letter.append((word[i], word.count(word[i])))
        elif word[i] not in word[:i] and i != 0:
            counter_letter.append((word[i], word.count(word[i])))
    return counter_letter


def get_words(f: str, letters: list[str]) -> list[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    legal_words = []
    with open(f, "r") as dictionary:
        for word in dictionary.readlines():
            if len(word[:-1]) >= 4 and letters[4] in word[:-1].lower():
                correct = True
                count_word = count_appearances(word[:-1].lower())
                for appearance in count_word:
                    if appearance[0] not in letters or appearance[1] > letters.count(
                        appearance[0]
                    ):
                        correct = False
                        break
                if correct and word[:-1].lower() not in legal_words:
                    legal_words.append(word[:-1].lower())
    return legal_words


def get_user_words() -> list[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    pass


def get_pure_user_words(
    user_words: list[str], letters: list[str], words_from_dict: list[str]
) -> list[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass


if __name__ == "__main__":
    print(get_words("en", ["e", "t", "x", "p", "h", "z", "o", "l", "i"]))

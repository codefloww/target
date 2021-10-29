'''module that handles the target game'''
import string
import random


def generate_grid():
    """Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]

    Returns:
        list[list[str]]: playing grid of letters
    """
    alphabet = string.ascii_uppercase
    letters_grid = [
        [alphabet[random.randint(0, 25)] for _ in range(3)] for _ in range(3)
    ]
    # check whether 5 different letters appear in grid
    unique = ""
    for row in range(3):
        for col in range(3):
            if letters_grid[row][col] not in unique:
                unique += letters_grid[row][col]
    if len(unique) < 5:
        letters_grid = generate_grid()

    return letters_grid


def display_grid(letters_grid) -> None:
    """Displays playing grid of letters

    Args:
        letters_grid (list[list[str]]): grid of letters
    """
    grid = ""
    for i in range(len(letters_grid)):
        grid += " ".join(letters_grid[i]) + "\n"
    print(grid[:-1])


def count_appearances(word: str):
    """Checks how many appearance of each letter in word

    Args:
        word (str): word to check

    Returns:
        list[tuple]: list of tuples('letter', appearances)
    """
    counter_letter = []
    word = word.lower()
    for i in range(len(word)):
        if i == 0:
            counter_letter.append((word[i], word.count(word[i])))
        elif word[i] not in word[:i] and i != 0:
            counter_letter.append((word[i], word.count(word[i])))
    return counter_letter


def check_rules(letters, word) -> bool:
    """checks whether word is legit due to rules of target game

    Args:
        letters (list[str]): letters of grid
        word ([type]): word to check for correctness

    Returns:
        bool: correctness of wor according to rules
    """
    correct = False
    if len(word) >= 4 and letters[4] in word.lower():
        correct = True
        count_word = count_appearances(word.lower())
        for appearance in count_word:
            if appearance[0] not in letters or appearance[1] > letters.count(
                appearance[0]
            ):
                correct = False
                break
    return correct


def get_words(file: str, letters):
    """gets all words from file(1 word per line) that
    are legit

    Args:
        f (str): file to get words from
        letters (list[str]): letters of grid

    Returns:
        list[str]: list of words that are with rules
    """
    legal_words = []
    with open(file, "r") as dictionary:
        for word in dictionary.readlines():
            if check_rules(letters, word[:-1]) and word[:-1].lower() not in legal_words:
                legal_words.append(word[:-1].lower())
    return legal_words


def get_user_words():
    """gets user words(1 per enter) until '' not entered

    Returns:
        list[str]: list of words from user
    """
    user_words = []
    word = "hi"
    print("Try to find some words)")
    while word != "":
        word = input()
        user_words.append(word)
    return user_words[:-1]


def get_pure_user_words(
    user_words, letters, words_from_dict):
    """Checks user words with the rules and returns list of those words
    that are not in dictionary.

    Args:
        user_words (list[str]): words from user
        letters (list[str]): letters of grid
        words_from_dict (list[str]): words which legit from dictionary

    Returns:
        list[str]: words that are with rules but not in dictinary
    """
    pure_user_words = []
    for word in user_words:
        if check_rules(letters, word) and word not in words_from_dict:
            pure_user_words.append(word)
    return pure_user_words


def results(
    words, legal_words, pure_words, file: str):
    """prints result of game to user and saves result in results.txt

    Args:
        words (list[str]): words from user
        legal_words (list[str]): words from dictionary that are legit
        pure_words (list[str]): words that legit to rules but not in dictionary
        file (str): file to save results to(will be created if don't exist)

    Returns:
        str: 5-line of results in results.txt
    """
    score = 0
    for word in words:
        if word in legal_words:
            score += 1
    print("Your score:" + str(score))
    print("Legal words:\n", legal_words)
    missed_words = []
    for word in legal_words:
        if word not in words:
            missed_words.append(word)
    print("You missed:\n", missed_words)
    print("Some mistakes:\n", pure_words)
    with open(file, "a") as res:
        res.write(str(score) + "\n")
        res.write(", ".join(legal_words) + "\n")
        res.write(", ".join(missed_words) + "\n")
        res.write(", ".join(pure_words) + "\n")
        res.write("=====" + "\n")


def main() -> None:
    """maintains a full process of game"""
    grid = generate_grid()
    display_grid(grid)
    letters = [
        grid[i][j].lower() for i in range(len(grid)) for j in range(len(grid[i]))
    ]
    legal_words = get_words("en", letters)
    user_words = get_user_words()
    pure_words = get_pure_user_words(user_words, letters, legal_words)
    results(user_words, legal_words, pure_words, "results.txt")


if __name__ == "__main__":
    main()

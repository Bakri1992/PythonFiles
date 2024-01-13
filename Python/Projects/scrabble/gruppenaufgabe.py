from itertools import permutations
import timeit
from math import floor

points = {
    "a": 1,
    "b": 3,
    "c": 4,
    "d": 1,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 2,
    "i": 1,
    "j": 6,
    "k": 4,
    "l": 2,
    "m": 3,
    "n": 1,
    "o": 2,
    "p": 4,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 6,
    "w": 3,
    "x": 8,
    "y": 19,
    "z": 3,
    "ä": 6,
    "ö": 8,
    "ü": 6,
    "": 0,
}


def get_wordlist():
    wordlist = set()
    with open("gruppenaufgabe\wordlist-german.txt", encoding="utf-8") as file:
        for word in file:
            word = word.lower().replace("\n", "")
            if len(word) <= 7:
                wordlist.add(word)
            # wordlist.add(word)
        return sorted(list(wordlist))


def get_permutations(letters):
    combinations = []
    for i in range(1, len(letters)):
        for p in permutations(letters, r=i):
            combinations.append("".join(p))
    return combinations


def search_list(wordlist, combinations):
    combinations = get_permutations(letters)
    possible_words = [comb for comb in combinations if comb in wordlist]
    return possible_words


def search_set(wordlist, combinations):
    wordlist = set(wordlist)
    combinations = get_permutations(letters)
    possible_words = {comb for comb in combinations if comb in wordlist}
    return possible_words

def binary_search(wordlist, comb):
    lower=0
    upper=len(wordlist)-1
    while lower < upper:
        m = floor((lower + upper)/2)
        if wordlist[m] < comb:
            lower = m + 1
        elif wordlist[m] > comb:
            upper = m - 1
        else:
            return True
    if wordlist[lower] == comb:
        return True
    else:
        return False


def binary_list(wordlist,combinations):
    possible_words = []
    for comb in combinations:
        if binary_search(wordlist, comb):
            possible_words.append(comb)
    return possible_words

def hash_func(word):
    value = ''
    for letter in word:
        value += str(ord(letter))
    return int(value)

def hash_search(wordlist, combinations):
    wordlist_dict = dict()
    for word in wordlist:
        if hash_func(word) in wordlist_dict.keys():
            print("Hash-Function values not unique.")
            exit()
        wordlist_dict[hash_func(word)] = word
    # wordlist = dict.fromkeys(wordlist)
    
    possible_words = []
    for comb in combinations:
        # if comb in wordlist.keys():
        #     possible_words.append(comb)
        if hash_func(comb) in wordlist_dict.keys():
            possible_words.append(comb)
    return possible_words

def calc_points(possible_words):
    suggestions = []
    for word in possible_words:
        pts = 0
        for l in word:
            pts += points[l]
        suggestions.append((word, pts))
    return suggestions


def create_output(possible_words):
    suggestions = calc_points(possible_words)
    suggestions.sort(key=lambda x: x[1], reverse=True)
    for w, p in suggestions:
        print(w)


if __name__ == "__main__":
    wordlist = get_wordlist()

    #letters = list(input("Kleinbuchstaben eingeben: "))
    test_letters = ["a","es", "tro", "kleg", "cerkd", "enehcs", "ührtsau"]

    for letters in test_letters:
        combinations = get_permutations(letters)

        # print(
        #     f"list: {timeit.timeit('search_list(wordlist, combinations)', globals=globals(), number=100_000)}"
        # )
        # print(
        #     f"set: {timeit.timeit('search_set(wordlist, combinations)', globals=globals(), number=100_000)}"
        # )
        # print(
        #     f"binary_list: {timeit.timeit('binary_list(wordlist, combinations)', globals=globals(), number=100_000)}"
        # )
        print(
            f"hash_dict: {timeit.timeit('hash_search(wordlist, combinations)', globals=globals(), number=100_000)}"
        )

    # possible_words_list = search_list(wordlist, combinations)
    # possible_words_set = search_set(wordlist, combinations)
    # possible_words_binary = binary_list(wordlist, combinations)
    # possible_words_hash = hash_search(wordlist, combinations)
        
    # create_output(possible_words_list)
    # print("-------------")
    # create_output(possible_words_set)
    # print("-------------")
    # create_output(possible_words_binary)
    # print("-------------")
    # create_output(possible_words_hash)

from itertools import permutations
import timeit


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


# Read the world list from a file and return it as a list(we should)
def Read_Wordlist():
    wordlist = set()
    path="C:/pf/Python/Python/Projects/scrabble/wordlist-german.txt"
    with open(path, 'r',encoding="utf-8") as f:
        for word in f:
            # Lets take the words with 2-7 letters
            # Number or words after filtering: 22354
            if len(word)<=7:
                wordlist.append(word.lower().strip())
                # Be careful "koko" != "koko\n"
                # We casted to lower case
    return wordlist

# Print all possible permutations from a word
def get_permutations(myword):
    word=myword
    combinations=[]
    for i in range(2,len(word)+1):
    # permutaions function returns me an iterable.
        for per in permutations(word,r=i):
            combinations.append("".join(per)) 
# Lets see how many permutations we have
    return combinations

def search_list(wordlist,combinations):
    possible_words=[]
    possible_words=[comb for comb in combinations  if comb in wordlist]
    return possible_words

def search_set(wordlist,combinations):
    possible_words=set()
    possible_words=set(comb for comb in combinations  if comb in wordlist)
    return possible_words

def binary_search(wordlist,comb):
    lower=0
    upper=len(wordlist)-1
    while lower<upper:
        m= (lower+upper)//2
        if(wordlist[m])<comb:
            lower=m+1
        elif(wordlist[m])>comb:
            upper=m-1
        else:
            return True
    if wordlist[lower]==comb:   # This happen when lower = upper maybe it happens when
                                # my searched object at first or last index!
        return True
    else:
        return False
    
def binary_list(wordlist,combinations):
    possible_words=[]
    for comb in combinations:
        if(binary_search(wordlist,comb)):
            possible_words.append(comb)
        return possible_words

# Lets define a hash function that takes a string and turn it into a hash number!
def hash_func(word):
    value=""
    for letter in word:
        value += str(ord(letter))
    return int(value)


def hash_search(wordlist, combinations):
    wordlist_dict=dict()
    for word in wordlist:
        if hash_func(word) in wordlist_dict.keys():
            print("Hash function value is not unique.")
        wordlist_dict[hash_func(word)]=word
    
    
    possible_words=[]
    for comb in combinations:
        if hash_func(comb) in wordlist_dict.keys():
            possible_words.append(comb)
            
    return possible_words



x=hash_func("Bakri")
print(ord("B"))
print(ord("a"))
print(ord("k"))
print(ord("r"))
print(ord("i"))
print(x)


# wordlist=Read_Wordlist()

# word="aalbezogenem"

































# for per in my_permutations:
#     print(per)
    
# print(len(my_permutations))
# lst =search_list(wordlist,my_permutations)
# # so=set(lst)
# print(lst)
# print(len(lst))

# set1=search_set(wordlist,my_permutations)
# print(len(my_permutations))
# print(len(set1))

# my_permutations=get_permutations(word)
# print(my_permutations)
# my_list=binary_list(wordlist,my_permutations)
# print(my_list)






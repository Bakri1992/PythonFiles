from itertools import permutations


# Read the world list from a file and return it as a list(we should)
def Read_Wordlist():
    wordlist = []
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

def binary_search(worldlist,comb):
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
    if wordlist[lower]==comb: # This happen when lower = upper maybe it happens when
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



wordlist=Read_Wordlist()

word="aalbezogenem"

my_permutations=get_permutations(word)
print(my_permutations)
my_list=binary_list(wordlist,my_permutations)
print(my_list)
































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







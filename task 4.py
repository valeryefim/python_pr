flag = False

def check(word1:str, word2: str) -> bool:
    if len(word1) != len(word2):
        flag = False
    return flag

def is_anagram(word1:str, word2: str) -> bool:
    counter = 0
    for letter1 in word1:
        for letter2 in word2:
            if letter1 == letter2:
                counter += 1
    return counter

word1 = input()
word2 = input()

check(word1, word2)
is_anagram(word1, word2)

if counter == len(word1):
    print("YES")
else:
    print("NO")
    ..

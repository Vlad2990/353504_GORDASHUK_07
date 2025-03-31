import math

def F(x, eps=0.0001):
    res = 1.0
    term = 1.0
    fres = math.cos(x)
    for i in range(1, 500):
        term *= (-1) * x * x / ((2 * i - 1) * (2 * i))
        res += term
        if abs(res - fres) < eps:
            break
    return res

def InputCycle():
    count = 0
    num = int(input())
    while num != 100:
        if num < 10:
            count += 1
        num = int(input())
    return count

def CheckString():
    numCount = 0
    charCount = 0
    for char in input():
        if char.isdigit():
            numCount += 1
        elif char.islower():
            charCount += 1
    return charCount, numCount

text = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."

words = text.split()
def FindConsonants():
    wordCount = 0
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    for word in words:
        if word[0] in consonants:
            wordCount += 1
    return wordCount

def FindTwoIdentical():
    word_pos = {}
    for word in words:
        for i in range(len(word)-1):
            if word[i].lower() == word[i+1].lower():
                word_pos[words.index(word)+1] = word
                break
    return word_pos

words2 = sorted(words, key=str.lower)

def FindHigher(arr, c):
    count = 0
    for num in arr:
        if num > c > 0:
            count += 1
    return count

def FindMul(arr):
    maxNum = max(arr)
    res = 1.0
    for num in arr[arr.index(maxNum)+1:]:
        res *= num
    return res

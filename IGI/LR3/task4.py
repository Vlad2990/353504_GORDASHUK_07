import string
from decorator import repeat_on_demand

"""
Lab Work #1
Gordashuk Vladislav
This module counts the number of words in a string that begin with a consonant,
searches for words containing two consecutive identical letters,
and outputs the words in alphabetical order.
Version: 1.0
Date: 30.03.2025
"""

def FindConsonants(words):
    """
    Count word which begin with a consonant

    Arg: list of string

    Return: Num pf words
    """
    wordCount = 0
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    for word in words:
        if word[0] in consonants:
            wordCount += 1
    return wordCount

def FindTwoIdentical(words):
    """
    Searches for words with two consecutive identical letters

    Arg: list of string

    Return: Dict of words and their positions
    """
    word_pos = {}
    for word in words:
        for i in range(len(word)-1):
            if word[i].lower() == word[i+1].lower():
                word_pos[words.index(word)+1] = word
                break
    return word_pos

@repeat_on_demand()
def Task4():
    print("\n" + "="*40)
    text = ("So she was considering in her own mind, as well as she could, "
        "for the hot day made her feel very sleepy and stupid, whether the "
        "pleasure of making a daisy-chain would be worth the trouble of "
        "getting up and picking the daisies, when suddenly a White Rabbit "
        "with pink eyes ran close by her.")
    print(text)
    clean_text = text.translate(str.maketrans('', '', string.punctuation))
    words = clean_text.split()
    print("\nNum of words, which begin with a consonant:", FindConsonants(words))
    print("\nWords with two identical letters and their pos:", FindTwoIdentical(words))
    words2 = sorted(words, key=str.lower)
    print("\nWords in alphabetical order:", words2)

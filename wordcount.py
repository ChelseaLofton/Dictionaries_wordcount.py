"""Count words in file."""

import sys

# put your code here.

# file = open("twain.txt")

file = open(sys.argv[1])

def tokenize(file):
    words = []
    for words in file:
        line = words.strip()
        words = line.split(" ")
        words.append(words)
    return words

def count_words(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        
    return word_count


def print_word_counts(word_count):
    for word, count in word_count.items():
        print(f"{word}: {count}")
    

tokenize(file)
count_words(tokenize)
print_word_counts(count_words)
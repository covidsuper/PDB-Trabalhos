#!/usr/bin/env python

import sys

def reducer():
    word_count = {}
    for line in sys.stdin:
        word, count = line.strip().split('\t')
        word_count[word] = word_count.get(word, 0) + int(count)

    for word, count in word_count.items():
        print(f"{word}\t{count}") 

if __name__ == "__main__":
    reducer()

#!/usr/bin/env python

import sys
import re

def mapper():
    for line in sys.stdin:
        words = line.strip().split()
        for word in words:
            if re.match(r"[A-Za-z]+", word):
                print(f"{word}\t1") 

if __name__ == "__main__":
    mapper()


#!/usr/bin/env python

import sys

# Função de mapeamento
def mapper():

    for line in sys.stdin:
        words = line.strip().split()
        for word in words:
            print(f"{word}\t1") 

if __name__ == "__main__":
    mapper()
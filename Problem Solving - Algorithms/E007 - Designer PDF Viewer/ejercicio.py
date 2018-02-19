# >>> Designer PDF Viewer
# >>> https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

#!/bin/python3

import sys

def designerPdfViewer(h, word):
    letraA = 97
    largo = len(word)
    palabra = [h[ord(x) - letraA] for x in word]
    alta = max(palabra)
    return alta * largo

if __name__ == "__main__":
    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7] #list(map(int, input().strip().split(' ')))
    word = 'zaba' #input().strip()
    result = designerPdfViewer(h, word)
    print(result)
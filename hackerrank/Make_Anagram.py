
from collections import Counter

def makeAnagram(a, b):
    c1, c2 = Counter(a), Counter(b)
    diff1 = c1 - c2
    diff2 = c2 - c1
    return sum((diff1 + diff2).values())

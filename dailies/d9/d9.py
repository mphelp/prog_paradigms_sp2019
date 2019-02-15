#!/usr/bin/python3

# Globals
MEMLIMIT = 10

myre = []
def plus(q):
    p = []
    chars = ""
    for i in range(MEMLIMIT):
        chars += q
        p.append(chars)
    return p
def star(q):
    p = []
    chars = ""
    for i in range(MEMLIMIT):
        p.append(chars)
        chars += q
    return p

if __name__ == '__main__':
    print(plus("4"))
    print(star("4"))

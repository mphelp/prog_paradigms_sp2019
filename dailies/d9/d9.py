#!/usr/bin/python3

# Globals
MEMLIMIT = 10


def join(myre, newExpr):
    if !isinstance(myre, list) or !isinstance(newExpr, list):
        print(f"ERROR: Expression parsed not a list: {newExpr}")

def plus(q):
    p = []
    chars = ""
    for i in range(MEMLIMIT):
        chars += q
        p.append(chars)
    return p
def star(q):
    s = []
    chars = ""
    for i in range(MEMLIMIT):
        s.append(chars)
        chars += q
    return s
def dot():
    return [c for c in "abcdefghijklmnopqrstuvwxyz"]
def add(expr, myre):
    if isinstance(expr, str):
        myre.append([expr])
    else:
        myre.append(expr)


if __name__ == '__main__':
    

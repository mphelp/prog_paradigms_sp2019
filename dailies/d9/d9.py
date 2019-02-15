#!/usr/bin/python3

# Globals
MEMLIMIT = 10


def join(newExpr, myre):
    if not isinstance(myre, list) or not isinstance(newExpr, list):
        print("ERROR: Expression parsed not a list")
    for option in newExpr:
        if len(myre) == 0:
            myre.append(option)
        else:
            for regex in myre:
                regex.append(option)

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
        join([expr], myre) 
    else:
        join(expr, myre) 

if __name__ == '__main__':
    myre = []
    add("a", myre)
    add(star("b"), myre) 
    print(myre)

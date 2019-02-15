#!/usr/bin/python3

# Globals
MEMLIMIT = 10

# Functions before evil
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
    return [c for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
def add(expr, myre):
    if isinstance(expr, str):
        newMyre = join([expr], myre) 
    else:
        newMyre = join(expr, myre) 
    return newMyre
def join(newExpr, myre):
    if not isinstance(myre, list):
        print("ERROR: Expression parsed not a list")
        return None
    if not isinstance(newExpr, list):
        print("ERROR: Myre parsed not a list")
        return None
    newMyre = []
    for option in newExpr:
        if len(myre) == 0:
            newMyre.append(option)
        else:
            for regex in myre:
                newRegex = regex + option
                newMyre.append(newRegex)
    return newMyre
def match(str, myre):
    return str in myre

# Functions after evil
def matchEvil(s, myre2):
    if not isinstance(s, str) or not isinstance(myre2, str):
        print('One arg in matchevil is not string')

def addEvil(s, myre2):
    return myre2 + s

if __name__ == '__main__':
    # Before evil
    myre = []
    myre = add(plus("cat"), myre)
    myre = add(dot(), myre)
    myre = add("d", myre)
    myre = add("o", myre)
    myre = add(star("g"), myre)
    print(match("catcatQdogggggg", myre))
    print(match("turkeybaconcheese", myre))

    # After evil
    myre2 = ""
    # print(matchEvil("acatcatccatcatdcatccatcatdcatccatcatd", myre2))
    print(addEvil("who",myre2))

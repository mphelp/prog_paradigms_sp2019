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
    return s == myre2

# addEvil("ab","c") -> "cab"
def addEvil(s, myre2):
    return myre2 + s
# evil("g","goggle") -> "ggg"
def evil(s, myre2):
    s2 = ""
    thiscount = myre2.count(s)
    for i in range(thiscount):
        s2 += s
    return s2

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
    regex1 = addEvil("acat",myre2)
    regex2 = evil("cat",regex1)
    regex3 = addEvil("c",addEvil(regex2,regex1))
    regex4 = evil("cat", regex3)
    regex5 = addEvil("d",addEvil(regex4,addEvil("c",addEvil(regex2,myre2))))
    regex6 = evil(regex5, addEvil(regex5, addEvil(regex5, addEvil(regex5, regex1))))
    regex7 = addEvil(regex6, regex1)
    
    print(matchEvil("acatcatccatcatdcatccatcatdcatccatcatd",regex7))


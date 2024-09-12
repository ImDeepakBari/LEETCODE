# Given two sting 's' , 't'. Return True if 't' is anagram of 's' else return false.
# eg : s= 'deepakbari' , t= 'barideepak'

def solution(s, t):
    if len(s) != len(t):
        return False

    hashmapS, hashmapT = {}, {}

    for i in range(len(s)):
        hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)
        hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)

    for ch in hashmapS:
        if hashmapS[ch] != hashmapT.get(ch, 0):
            return False

    return True

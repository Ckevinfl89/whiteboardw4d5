#Given two strings containing only capital and lowercase letters, write a function that returns true if they are anagrams of each other and false otherwise.
#An anagram is a word, phrase, or name formed by rearranging the letters of another word.

# s1 = "anagram"
# t1 = "nagaram"
# Output:
# True

#s2 = "rat"
#t2 = "car"
#Output:
# False

#s3 = "stops"
#t3 = "pots"
#Output:
# False


def solution(inputStr, testStr):

    if len(inputStr) != len(testStr):
        return False

    stringLower = inputStr.lower()
    testLower = testStr.lower()

    stringDict = {}
    for c in stringLower:
        if c not in stringDict.keys():
            stringDict[c] = 1
        else:
            stringDict[c] += 1

    for c2 in testLower:
        if c2 not in stringDict.keys():
            return False
        else: #if the char is found
            if stringDict[c2] <= 0:
                return False
            else:
                stringDict[c2] -= 1
    return True


def solution(s, t):
    pat = re.compile('\w')
    striped_s = pat.findall(s.lower())
    set_s = set(striped_s)
    for l in set_s:
        if striped_s.count(l) != t.lower().count(l):
            return False
    return True


def solution(string1, string2):
    return sorted(string1.lower()) == sorted(string2.lower())
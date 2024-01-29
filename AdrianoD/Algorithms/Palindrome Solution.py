# The algorithm passed all testcases except x = 0, it returns None instead of True.  Why is this?
def isPalindrome(x: int) -> bool:
    if x != abs(x):
        return False

    i = 0
    s = str(x)
    j = len(s) - 1

    while i < len(s):
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
        if i == j:
            return True
 

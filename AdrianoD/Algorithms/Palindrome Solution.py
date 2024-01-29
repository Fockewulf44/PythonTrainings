# The algorithm prints x = 11 as None.
def isPalindrome(x: int) -> bool:
    if x != abs(x):
        return False

    i = 0
    s = str(x)
    j = len(s) - 1
    while i < len(s):
        if i == j or i > j:
            return True  
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return False      
print(isPalindrome(11))



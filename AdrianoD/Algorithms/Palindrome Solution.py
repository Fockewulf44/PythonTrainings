def isPalindrome(x: int) -> bool:
    if x == abs(x):
        return True

    i = 0
    j = len(str(x)) - 1
    s = str(x)

    while i < len(s):
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    if i == j:
        return True

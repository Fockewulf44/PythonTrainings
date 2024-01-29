def isPalindrome(x: int) -> bool:
    # Why does it return True? It should return false ONLY
    # if the number is negative
    if x == abs(x):
        return True

    i = 0    
    s = str(x)
    j = len(s) - 1

    while i < len(s):
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    # This IF must be inside While loop
    # But currently it is not inside
    if i == j:
        return True

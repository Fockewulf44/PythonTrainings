# The algorithm passed all testcases except x = 0, it returns None instead of True.  Why is this?
# Answer -> your function doesn't have any default. So, it should return False by dfault
def isPalindrome(x: int):
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

    # Here your function should return False in case if it doesn't return true
    # Try also debug the code. Put a breakpoint and debug and see how it goes
 
 
print(isPalindrome(0))

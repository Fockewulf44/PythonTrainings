def isPowerOfTwo(n: int) -> bool:
        x = 0
        while x < n: 
            if n == pow(2, x):
                return True
        else:
            return False
        x += 1
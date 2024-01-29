def isPowerOfTwo(n: int) -> bool:
        x = 0
        if n == pow(2, x):
            return True
        if n != pow(2, x):
            return False
        x += 1
        breakpoint()

print(isPowerOfTwo(16))
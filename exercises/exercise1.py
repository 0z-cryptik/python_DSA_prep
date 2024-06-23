# Write a short Python function, is_multiple(n, m), that takes two integer values and returns True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.


def is_multiple(n, m):
    if n % m:
        return False
    else:
        return True
    
print(is_multiple(20, 2))

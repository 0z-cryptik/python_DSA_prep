# Give a single command that computes the sum from the previous exercise, relying on Python’s comprehension syntax and the built-in sum function.

def mi_function(n):
    return sum([i * i for i in range(n)])


print(mi_function(500))

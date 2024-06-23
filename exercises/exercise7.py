# Give a single command that computes the sum from thr previous exercise, relying on Python’s comprehension syntax and the built-in sum function.

def mi_function(n):
    return sum([i for i in range(n) if i % 2 != 0])


print(mi_function(50))

# Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.

def mi_function(n):
    if type(n) != int:
        raise TypeError('the parameter must be a positive integer')
    if n < 0:
        raise ValueError('the parameter must be greater than 0')
    
    squares = []

    for i in range(n):
        if i % 2 != 0:
            squares.append(i)
    
    return sum(squares)
    

print(mi_function(50))
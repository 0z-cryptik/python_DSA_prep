# Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.

def minmax(data):
    if len(data) < 1:
        raise IndexError('parameter must have at least one number')

    for i in data:
        if not isinstance(i, int) | isinstance(i, float):
            raise TypeError('values in the sequence must be numeric')

    biggest = 0

    for j in data:
        if j > biggest:
            biggest = j

    smallest = biggest

    for k in data:
        if k < smallest:
            smallest = k

    return biggest, smallest

mi_list = [1,2,3,4,5,6]
one_number = [5]

print(minmax(mi_list))
print(minmax(one_number))

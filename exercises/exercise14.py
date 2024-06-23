# Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other (that is, they are distinct).

def all_different(data):
    for i in data:
        if not isinstance(i, int):
            raise TypeError('values must be integers')
    if len(data) < 1:
        raise IndexError('the parameter cannot be an empty sequence')
    elif len(data) == 1:
        return False

    count = 0
    for j in data:
        for k in data:
            if k == j:
                count += 1
    if count > len(data):
        return False
    else:
        return True


same = [1, 2, 2, 4, 5]
different = [1, 2, 3, 4, 5]

print(all_different(same))
print(all_different(different))

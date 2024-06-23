# Write a short Python function that counts the number of vowels in a given character string.


def how_many_vowels(data):
    if not isinstance(data, str):
        raise TypeError('parameter has to be a string')
    elif len(data) < 1:
        raise ValueError('parameter cannot be an empty string')

    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for i in data:
        for j in vowels:
            if i == j:
                count += 1

    return count


print(how_many_vowels('aeroplane'))

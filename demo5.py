if 2 >= 0:
    a = True
else:
    a = False

# the above can be rewritten as
a = True if 2 >= 0 else False


def squares(n):
    squares_list = []
    for i in range(1, n+1):
        squares_list.append(i * i)
    return squares_list

# print(squares(30))

# the above function can be achieved like this
# this method can also be used by sets, dicts and generators (no tuples)


def squares2(n):
    squares_list = [i*i for i in range(1, n+1)]
    return squares_list


# print(squares2(30))


def factors(n):
    factors_list = [f for f in range(1, n+1) if n % f == 0]
    return factors_list


print(factors(100))

# this is considered a tuple
data = 2, 3, 5, 8, 11


# a = 8, b = 9...
a, b, c, d = 8, 9, 10, 11

# can also be achieved with
a, b, c, d = range(8, 12)
# this unpacking/destructuring method works for any iterable type, here c = 't'
a, b, c = 'cat'

print(c)

mi_dict = {
    "name": "kamp billy",
    "age": 22,
    "height": "5'5",
    "job": "arms dealer"
}

# i = key, j = value
for i, j in mi_dict.items():
    print(i, j, sep=': ')

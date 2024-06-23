temperature = 98.6
original = temperature

# no longer points at 96, but original still does
temperature = 12

print(temperature, original)

mi_list = [1, 5, 2, 3, 4]
mi_list.sort()

print(mi_list)

foo = 0

if bool(foo):
    print('foo is truthy')
else:
    print('foo is falsy')

# converts string 12 to number 12
number_int = int('12')
# converts base 2 string 011 to base 10 number
print(int('011', 2))
# converts string 12 to float 12.0
print(float('12'))

mi_tuple = (14,)
print(mi_tuple)

# this produces an empty set, {} produces an empty dict
mi_set = set()

mi_set.add('thor')
mi_set.add('odin')
print(mi_set)

mi_set = {'poseidon', 'zues', 'athena', 'hera'}
print(mi_set)

# set cannot have duplicates, therefore this returns {h, e, l, o} in no particular order
print(set('hello'))

# this is a dict, difference from set is that set doesn't have keys
mi_dict = {
    'club': 'manchester UTD',
    'legend': 'paul scholes',
    'home': 'old trafford'
}

print(mi_dict)

# can also create a dict from ready made pairs (must be pairs)
pairs = [
    ('club', 'chelsea'),
    ('legend', 'frank lampard')
]

print(dict(pairs))

#print(list(range(1, 1001, 5)))
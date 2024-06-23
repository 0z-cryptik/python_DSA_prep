word1 = 'valar'
word2 = 'morghulis'
word1_and_2 = word1 + word2

print(word1_and_2)

check_truthy = bool(word1 and word2)

print(check_truthy)

check_containment = bool('vala' in word1)
print(check_containment)

check_difference = bool(word1 is not word2)

print(check_difference)

check_equality = bool(word1 == word2)

print(check_equality)

set1 = {2, 33, 14, 22}
set2 = {22, 14, 33, 2}

# this is truthy
check_set_equality = bool(set1 == set2)
# this is falsy, even when arranged in the same order
check_set_equality2 = bool(set1 is set2)

# lowercase is always greater than uppercase no matter how many letters the uppercase has
print(bool('hello' > 'HELLO'))

# when both strings are lowercase the comparison is done in lexicographic order
print(bool('z' > 'a'))

division = 27/4  # returns the result (as a float)

# only returns an integer (ignores the floating point when there's one), unless the dividend or the divisor is a float
return_int = 27//4
remainder = 27 % 4  # returns the remainder of the calculation

print(division, return_int, remainder, 8.2//3.14)

mi_list = [12, 33, 44, 45]
every_item = mi_list[0:]
last_item = mi_list[-1]
second_to_last_item = mi_list[-2]

# in a [a:b] expression, value at a is included in result while one at b isn't
item_0_to_2 = mi_list[0: 3]
item_0_to_2 = mi_list[:3]
item_2_to_last = mi_list[2:]
item_1_to_3 = mi_list[1:4]

mi_list2 = ['hey', 'you', 'hi']
joined_list = (mi_list2 + mi_list)

# lists can also be mutated by anotating new values to their slices
new_list = [2, 8, 9, 7, 22, 16]
new_list[2] = 500
new_list[3:] = ["one", "two", "three"]
print(new_list)

# COMPARISON FOR SETS

set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4}
# this checks if set2 is a subset of set1 (the other way round checks if set1 is a superset of set2)
subset_check = bool(set2 < set1)
# this checks if it's a subset or has the same values
subset_check2 = bool(set2 <= set1)
print(subset_check)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1_and_2 = set1 | set2
# returns the only value present in set 1 and 2
set_intersection = set1 & set2
# returns the values present in only set1 and not set2
only_set1 = set1 - set2
print(set1_and_2, only_set1)

# 2 is the step, meaning it prints in increments of 2 instead of 1
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[0:-1: 2])

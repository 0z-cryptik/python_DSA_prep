data = ['a', 'b', 'c', 'd', 'e']

j = 0

while j < len(data) and data[j] != 'e':
    print(data[j])
    j += 1

# can be rewritten as
for each_value in data:
    if (each_value != 'e'):
        print(each_value)

data = [1, 2, 3, 4, 5, 65, 6]

# an algorithm to get the biggest number in a list


def return_biggest(list):
    biggest = 0
    for value in list:
        if value > biggest:
            biggest = value
    return biggest


print(return_biggest(data))

# an algorithm to get where the biggest value is
location_of_biggest_value = 0
for i in range(len(data)):
    if data[i] > data[location_of_biggest_value]:
        location_of_biggest_value = i

print(location_of_biggest_value)

# DEFAULT PARAMETERS


def foo(a = 0, b=1, c=2):
    print(a, b, c)


# python supports keyword argument i.e I can choose which parameter I give a value
# this assigns b to 35
foo(b=35)
# while this assigns a to 35
foo(35)

for i in range(1, 5):
    print("yolo", i)

mi_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
reversed_list = reversed(mi_list)
print(sorted(mi_list))



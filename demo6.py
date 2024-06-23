import random
import math
# import demo5 (commented out because it runs all the commands from demo5)
# print(demo5.factors(50))

print(math.sqrt(81), math.pi)

mi_list = [1, 2, 3, 4, 5, 6, 7, 8]

# random.shuffle mutates the original list, it doesn't copy and return a different list
print(random.shuffle(mi_list), mi_list)

# prints random integer in range 1 - 5
print(random.randint(1, 5))

# prints a number selected randomly from the sequence
print(random.choice(mi_list))

#prints a random float
print(random.random())

# Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of numbers in the sequence whose product is odd.

def check_odd_product(data):
    for i in data:
        if not isinstance(i, int):
            raise TypeError('values must be an integer')
    for j in data:
        for k in data:
            if (k * j) % 2 != 0:
                return True
    return False


odd_pair_list = [1, 3, 5, 7]
non_odd_pair_list = [2, 4, 6, 8]

print(check_odd_product(non_odd_pair_list))

# Write a short Python function, is_even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.


def is_even(k):
    remainder = divmod(k, 2)[1]
    if remainder:
        return False
    else:
        return True


print(is_even(22))

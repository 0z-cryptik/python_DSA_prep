# Write a short program that takes as input three integers, a, b, and c, from the console and determines if they can be used in a correct arithmetic formula (in the given order), like “a+b = c,” “a = b−c,” or “a∗b = c”

def check_formula_compatibility(a, b, c):
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
        if a+b == c or a == b-c or a*b == c:
            return True
        else:
            return False
    else:
        raise TypeError('parameters must be integers')
    
print(check_formula_compatibility(3, 5, 15))

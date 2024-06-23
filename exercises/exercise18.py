# Write a Python program that can take a positive integer greater than 2 as input and write out the number of times one must repeatedly divide this number by 2 before getting a value less than 2.

def how_many_times_div_by_2(n):
    if type(n) != int:
        raise TypeError('parameter must be an integer')
    if n < 2:
        raise ValueError('parameter must be greater than 2')
    
    new_figure = n
    count = 0

    while True:
        if new_figure > 2:
            count += 1
            new_figure = new_figure / 2
        else:
            break

    return count

print(how_many_times_div_by_2(24))
    
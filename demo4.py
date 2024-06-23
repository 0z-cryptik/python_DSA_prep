# instead of separating with space, it separates with a :
print('name', 'Eniitan', sep=': ')


def tell_who_you_are():
    user_input = input("who are you? ")
    print("This user is the", user_input.split()[-1])

# tell_who_you_are()


fp = open('file.txt')
# print(fp.read())


def file_appender(the_file, content):
    fp = open(the_file, 'a')
    fp.write(content)
    fp.close()
    edited_file = open(the_file)
    print(edited_file.read())

# file_appender('file.txt', '\nKanye West is a god\n')


def type_checker(arg: str):
    # can also be achieved with: if (not isinstance(arg, str))
    if (type(arg) != str):
        raise TypeError('argument has to be a string')
    elif (len(arg) <= 0):
        raise ValueError('argument cannot be an empty string')
    else:
        print(arg)

# type_checker(100)


def age_error_handling():
    try:
        age = int(input('input your age > '))
        if age <= 0:
            print('your age must be above zero')
        else:
            print('You are', age, 'years old')
    except Exception as e:
        print('Ivalid response, check error message below\n', e)


# age_error_handling()

def return_factors(number):
    results = []
    for i in range(1, number + 1):
        if number % i == 0:
            results.append(i)
    return results

# print(return_factors(1000))

# to create a generator


def factors(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


factors_list = []
for i in factors(50):
    factors_list.append(i)
print(factors_list)

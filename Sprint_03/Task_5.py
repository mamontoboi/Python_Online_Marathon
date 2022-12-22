# Create decorator logger. The decorator should print to the console information about function's name and all its arguments separated with ',' for the function decorated with logger.
#
# Create function concat with any numbers of any arguments which concatenates arguments and apply logger decorator for this function.
#
# For example
#
# print(concat(2, 3)) display
# Executing of function concat with arguments 2, 3...
# 23
#
# print(concat('hello', 2)) display
# Executing of function concat with arguments hello, 2...
# hello2
#
# print(concat (first = 'one', second = 'two')) display
# Executing of function concat with arguments one, two...
# onetwo

def logger(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        params = ', '.join([str(i) for i in args])
        params_kwags = ', '.join([str(i) for i in kwargs.values()])
        if params_kwags and params:
            final_param = params + ', ' + params_kwags
        elif params and not params_kwags:
            final_param = params
        elif params_kwags and not params:
            final_param = params_kwags
        print("Executing of function {} with arguments {}...".format(func.__name__, final_param))
        while func.__name__ != 'print_arg':
            return func(*args, **kwargs)

    return wrapper


@logger
def concat(*args, **kwargs):
    string = ''
    for i in args:
        string += str(i)
    for j in kwargs.values():
        string += str(j)
    return string


@logger
def sum(a,b):
    return a+b


@logger
def print_arg(arg):
    print(arg)


# Executing of function concat with arguments 1...
# 1
print(concat(1))
print(concat('hello', 2))

# Executing of function concat with arguments first string, 2, second string...
# first string2second string
print(concat('first string', second=2, third='second string'))
print(sum(2,3))
print_arg(2)

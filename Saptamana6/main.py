def my_intial_function(msg):
    print(msg)

def another_function(function_param):
    function_param('Hello World!')

another_function(my_intial_function())


def sum_from_args(*args):
    s = 0

    for n in args:
        s += n

    return s

def sum_decorator(function_to_decorate):
    def wrapper(*args):
        print("Do something before function call...")
        function_result = function_to_decorate(*args)
        print("Do something after function call...")

        return function_result

    return wrapper

def multiply_by_decorator(number):
    def function_wrapper(function_to_decorate):
        def wrapper(*args):
            print("Do something before function call...")
            result = function_to_decorate(*args)
            print("Do something after function call...")

            return result * number

        return wrapper
    return function_wrapper


@sum_decorator
def sum_from_args(*args):
    s = 0

    for n in args:
        s+=n

    return s

my_sum = sum_from_args(1, 2, 3)
print(my_sum)


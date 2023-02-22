# a = [2, 3, 4, 5]
# iterator = iter(a)
# print(iterator)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
#
# for i in iterator:
#     print(i)
#
#
# for j in a:
#     print(j)


# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
#
#
# count = Counter(5)
# for i in count:
#     print(i)


# def generator(number, max_degree):
#     i = 0
#     for _ in range(max_degree):
#         yield number**i
#         i += 1
#
# res = generator(124, 100)
# print(res)
# for i in res:
#     print(i)

# i = 0
# while True:
#     print(i**100)
#     i += 1


# def generator(number):
#     i = 0
#     while True:
#         yield number ** i
#         i += 1
#
#
# res = generator(12345)
# for i in res:
#     print(i)
def make_decorator(*exc_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except (exc_types) as e:
                print(f"We have problems {e}")
            else:
                    print(f"No problems. Result -  {result}")
        return wrapper
    return decorator


@make_decorator(NameError, TypeError, SyntaxError)
def calculate(expression):
    return eval(expression)


calculate("2+2")








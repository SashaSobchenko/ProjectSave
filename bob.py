# import logging

# logging.basicConfig(level=logging.DEBUG, filename='logs.log', filemode='w', format="We have next logging message: %(asctime)s : %(levelname)s - %(message)s")
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')

# try:
#     print(10/0)
# except Exception:
#     logging.exception("Exception")

# x = 4
# y = 5
# logging.info(f'The values of x and y are {x} and {y}')
# try:
#     result = x/y
#     logging.info(f"x/y successful with result {result}")
# except Exception as e:
#     logging.error('Exception', exc_info=True)

# x_elem = [2, 3, 4, 6, 10]
# y_elem = [5, 7, 12, 0, 1]
#
# # for x_e, y_e in zip(x_elem, y_elem):
#     x, y = x_e, y_e
#     logging.info(f'The values of x and y are {x} and {y}')
#     try:
#         result = x/y
#         logging.info(f"x/y successful with result {result}")
#     except ZeroDivisionError as e:
#         logging.exception("ZeroDivisionError")
#
#
# a = zip(x_elem, y_elem)
# print(a.__next__())
# print(a.__next__())
# print(tuple(a))


# assert 2+2 == 5
# """
# >> 2+2
# 4
# """
#
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

def adder(*args, **kwargs):
    result = 0
    for arg in args:
        if type(arg) == int or type(arg) == float:
            result += arg
        else:
            try:
                result += float(arg)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(arg)
                continue
            except (ValueError, TypeError):
                pass
    for value in kwargs.values():
        if type(value) == int or type(value) == float:
            result += value
        else:
            try:
                result += float(value)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(value)
                continue
            except (ValueError, TypeError):
                pass
    return result

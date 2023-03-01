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
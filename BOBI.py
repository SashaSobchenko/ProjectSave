def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_seq = fib()  # ітерований об'єкт, який повертає генератор

# ітеруємося по послідовності чисел Фібоначчі та друкуємо їх на екран
for i in range(10):
    print(next(fib_seq))
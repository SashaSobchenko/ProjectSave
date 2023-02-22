import random
num = random.randint(1, 100)


class NumberProcessor:
    def __init__(self, num):
        self.__num = num

    def __process(self):
        operation = random.choice(["+", "-", "*", "/"])
        if operation == "+":
            return self.__num + random.randint(1, 100)
        elif operation == "-":
            return self.__num - random.randint(1, 100)
        elif operation == "*":
            return self.__num * random.randint(1, 10)
        elif operation == "/":
            return self.__num / random.randint(1, 10)

    def __str__(self):
        return str(self.__process())


processor = NumberProcessor(num)
print('Result: ', processor)
print("Encrypted number: ", num)

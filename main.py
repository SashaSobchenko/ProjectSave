# class Student:
#     def __init__(self, h, name):
#         self.name = name
#         self.height = h
#
#     def set_height(self, height):
#         self.height = height
#
#     def get_height(self):
#         print(self.height)
#
#     def __str__(self):
#         return f"I'm a student. My name is {self.name}"
#
#     def __del__(self):
#         print('Game over')
#
#
# Sasha = Student(170, name="Sasha")
#
# Sasha.get_height()
# Sasha.set_height(185)
# Sasha.get_height()
#
# print(Sasha)
import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print('Time to study')
        self.gladness -= 3
        self.progress += 0.12

    def to_chill(self):
        print('Rest time')
        self.gladness += 5
        self.progress -= 0.1

    def to_sleep(self):
        print('Time to sleep')
        self.gladness += 3

    def is_alive(self):
        if self.progress < - 0.5:
            print('Cast out...')
            self.alive = False
        elif self.gladness <= 0:
            print('Depression...')
            self.alive = False
        elif self.progress > 5:
            print('Passed exams')
            self.alive = False

    def day_info (self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + ' of ' + self.name + ' life'
        print(f'{day:=^50}')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_chill()
        else:
            self.to_sleep()
        self.day_info()
        self.is_alive()


Sasha = Student("Sasha")

for day in range(1, 366):
    if Sasha.alive == False:
        break
    Sasha.live(day)









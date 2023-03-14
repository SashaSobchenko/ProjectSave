import random


class Human:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_read(self):
        print('Time to read')
        self.gladness -= 3
        self.progress += 0.12

    def to_play(self):
        print('Play time')
        self.gladness += 5
        self.progress -= 0.1

    def to_sleep(self):
        print('Time to sleep')
        self.gladness += 3

    def is_alive(self):
        if self.progress < - 0.5:
            print('Tilt...') #Tilt обиделся на все и не хочет ничего делать
            self.alive = False
        elif self.gladness <= 0:
            print('So sad =(')
            self.alive = False
        elif self.progress > 5:
            print('Very good...')
            self.alive = False

    def day_info (self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + ' of ' + self.name + ' life'
        print(f'{day:=^50}')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_read()
        elif live_cube == 2:
            self.to_play()
        else:
            self.to_sleep()
        self.day_info()
        self.is_alive()


Bobik = Human("Bobik")

for day in range(1, 366):
    if Bobik.alive == False:
        break
    Bobik.live(day)
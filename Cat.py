import random


class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_run(self):
        print('Time to run')
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
            print('So sad =(')
            self.alive = False
        elif self.progress > 5:
            print('Fast run...')
            self.alive = False

    def day_info (self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + ' of ' + self.name + ' life'
        print(f'{day:=^50}')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_run()
        elif live_cube == 2:
            self.to_chill()
        else:
            self.to_sleep()
        self.day_info()
        self.is_alive()


Bob = Cat("Bob")

for day in range(1, 366):
    if Bob.alive == False:
        break
    Bob.live(day)
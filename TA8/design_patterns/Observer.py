from TA5.python.Stack import Stack


class Observable:
    def notify(self):
        raise NotImplementedError("")

    def __update(self):
        raise NotImplementedError("")


class Number1(Observable):
    def __init__(self, num: int):
        self.value = num

    def notify(self):
        print("Number 1 notified!")
        self.__update()

    def __update(self):
        self.value += 1
        print("Number 1: " + str(self.value))


class Number2(Observable):
    def __init__(self, num: int):
        self.value = num

    def notify(self):
        print("Number 2 notified!")
        self.__update()

    def __update(self):
        self.value -= 1
        print("Number 2: " + str(self.value))


class Number3(Observable):
    def __init__(self, num: int):
        self.value = num

    def notify(self):
        print("Number 3 notified!")
        self.__update()

    def __update(self):
        self.value *= 2
        print("Number 3: " + str(self.value))


class Observer:
    def __init__(self):
        self.__observed = []

    def add_observable(self, obs: Observable):
        self.__observed.append(obs)

    def notify_all(self):
        for obs in self.__observed:
            obs.notify()


obs = Observer()
obs.add_observable(Number1(100))
obs.add_observable(Number2(100))
obs.add_observable(Number3(1))
for i in range(10):
    obs.notify_all()

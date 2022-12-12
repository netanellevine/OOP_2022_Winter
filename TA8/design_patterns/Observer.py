from TA5.python.Stack import Stack


class Observer:
    def notify(self):
        raise NotImplementedError("")

    def __update(self):
        raise NotImplementedError("")


class Number1(Observer):
    def __init__(self, num: int):
        self.value = num

    def notify(self):
        print("Number 1 notified!")
        self.__update()

    def __update(self):
        self.value += 1
        print("Number 1: " + str(self.value))


class Number2(Observer):
    def __init__(self, num: int):
        self.value = num

    def notify(self):
        print("Number 2 notified!")
        self.__update()

    def __update(self):
        self.value -= 1
        print("Number 2: " + str(self.value))


class Number3(Observer):
    def __init__(self, num: int):
        self.value = num

    def notify(self):
        print("Number 3 notified!")
        self.__update()

    def __update(self):
        self.value *= 2
        print("Number 3: " + str(self.value))


class Observable:
    def __init__(self):
        self.__observed = []

    def add_observer(self, observer: Observer):
        self.__observed.append(observer)

    def notify_all(self):
        for observer in self.__observed:
            observer.notify()


obs = Observable()
obs.add_observer(Number1(100))
obs.add_observer(Number2(100))
obs.add_observer(Number3(1))
for i in range(10):
    obs.notify_all()

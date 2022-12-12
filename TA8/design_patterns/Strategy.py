class Strategy:
    def execute(self, my_input: int):
        raise NotImplementedError("")


class NoStrategy(Strategy):
    def execute(self, my_input: int):
        return my_input


class IncreaseStrategy(Strategy):
    def execute(self, my_input: int):
        my_input += 1
        return my_input


class DecreaseStrategy(Strategy):
    def execute(self, my_input: int):
        my_input -= 1
        return my_input


x = 10
strategies = [NoStrategy(), IncreaseStrategy(), DecreaseStrategy()]  # list of strategy

# Mixed strategies
print("Mixed")
for i in range(3):
    print(strategies[i].execute(x))

# No strategy
print("No strategy")
for i in range(5):
    x = strategies[0].execute(x)
    print(x)

# Increase strategy
print("Increase")
for i in range(5):
    x = strategies[1].execute(x)
    print(x)

# Decrease strategy
print("Decrease")
for i in range(5):
    x = strategies[2].execute(x)
    print(x)

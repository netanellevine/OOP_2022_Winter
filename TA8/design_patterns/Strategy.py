class Strategy:
    def execute(self, input: int):
        raise NotImplementedError("")


class NoStrategy(Strategy):
    def execute(self, input: int):
        return input


class IncreaseStrategy(Strategy):
    def execute(self, input: int):
        input += 1
        return input


class DecreaseStrategy(Strategy):
    def execute(self, input: int):
        input -= 1
        return input


input = 10
strategies = [NoStrategy(), IncreaseStrategy(), DecreaseStrategy()]  # list of strategy

# Mixed strategies
# print("Mixed")
# for i in range(3):
#     print(strategies[i].execute(input))

# No strategy
# print("No strategy")
# for i in range(5):
#     input = strategies[0].execute(input)
#     print(input)

# Increase strategy
# print("Increase")
# for i in range(5):
#     input = strategies[1].execute(input)
#     print(input)

# Decrease strategy
# print("Decrease")
# for i in range(5):
#     input = strategies[2].execute(input)
#     print(input)

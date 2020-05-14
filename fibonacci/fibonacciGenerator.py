def generateFibonacciSequence(position: int) -> int:
    if position == 0 or position == 1:
        return position
    return generateFibonacciSequence(position - 1) + generateFibonacciSequence(position - 2)


########################
#   BONUS SPEED TEST   #
########################
# Class from comment on https://stackoverflow.com/questions/1988804/what-is-memoization-and-how-can-i-use-it-in-python
class Memoize:
    def __init__(self, function):
        self.function = function
        self.memory = {}

    def __call__(self, *args):
        if not args in self.memory:
            self.memory[args] = self.function(*args)
        return self.memory[args]

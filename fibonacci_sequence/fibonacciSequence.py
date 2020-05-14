import functools

from fibonacci_generator import fibonacciGenerator


def getListOfSequentialValues(number: int) -> []:
    fibonacciGenerator.getValueFor = fibonacciGenerator.Memoize(fibonacciGenerator.getValueFor)
    result = []
    for i in range(number):
        result.append(fibonacciGenerator.getValueFor(i))
    return result


def generateFibonacciSequence(position: int) -> int:
    if position == 0 or position == 1:
        return position
    return generateFibonacciSequence(position - 1) + generateFibonacciSequence(position - 2)

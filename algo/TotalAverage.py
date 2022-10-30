class MovingAverage(object):
    """
    Calculating average of a list with sliding window
    """
    def __init__(self, size):
        """

        Args:
            size (int): 
        """
        self.size = size
        self.moves = [] * size

    def next(self, val):
        """
        return the average
        Args:
            val (int):

        Returns:

        """
        self.moves.append(val)
        if len(self.moves) > self.size:
            self.moves = self.moves[1:]
        total = 0.0
        for m in self.moves:
            total += m
        return (float)(total / len(self.moves))


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

m = MovingAverage(3)  # init the window to size 3
print(m.next(1))  # = 1 / 1
print(m.next(10))  # = (1 + 10) / 2
print(m.next(3))  # = (1 + 10 + 3) / 3
print(m.next(5))  # = (10 + 3 + 5) / 3

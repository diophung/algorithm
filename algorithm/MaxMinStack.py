import sys


class StackMinMax:
    def __init__(self):
        self.size = 100
        self.items = []
        self.max_items = [-sys.maxsize]
        self.min_items = [sys.maxsize]

    def push(self, number):
        self.items.append(number)
        
        if number > self.max_items[len(self.max_items) - 1]:
            self.max_items.append(number)
        
        if number < self.min_items[len(self.min_items) - 1]:
            self.min_items.append(number)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        top_of_stack = self.items[len(self.items) - 1]
        if top_of_stack == self.max_items[len(self.max_items) - 1]:
            self.max_items.pop()
        if top_of_stack == self.min_items[len(self.min_items) - 1]:
            self.min_items.pop()
        return top_of_stack 

    def peek(self):
        return self.items[len(self.items) - 1]

    def getMax(self):
        return self.max_items[len(self.max_items) - 1]

    def getMin(self):
        return self.min_items[len(self.min_items) - 1]

stack = StackMinMax()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(1)
print(stack.pop())
print(stack.peek())
print(stack.getMin())
print(stack.getMax())
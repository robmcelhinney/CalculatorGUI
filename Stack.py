from Calculator import *

# Class for a stack.
class Stack:
    # Main constructor.
    def __init__(self):
        self._items = []
    # Method for moving an item into the stack.
    def push(self, item):
        self._items.append(item)
    # Method for removing and returning the last item in the stack.
    def pop(self):
        if len(self._items) == 0:
            return None
        return self._items.pop()
    # Method for returning the length of the stack.
    def size(self):
        return len(self._items)
    # Method for returning a boolean if the stack is empty or not.
    def isEmpty(self):
        return self._items == []
    # Method for adding the number in the stack together and returning
    # the answer.
    def add(self, base):
        value = 0
        if self.size() >= 2:
            while self.size() > 0:
                value += int(self.pop())
        if base in range(2,9):
            value = self.convertToBase(value, base)
        return value
    # Method for subtracting the number in the stack together and
    # returning the answer.
    def subtract(self, base):
        reverse = Stack()
        while self.size() > 0:
            reverse.push(int(self.pop()))
        value = reverse.pop()
        while reverse.size() > 0:
            value -= reverse.pop()
        if base in range(2,9):
            value = self.convertToBase(value, base)
        return value
    # Method for multiplying the number in the stack together and
    # returning the answer.
    def multiply(self, base):
        reverse = Stack()
        while self.size() > 0:
            reverse.push(int(self.pop()))
        value = reverse.pop()
        while reverse.size() > 0:
            value *= reverse.pop()
        if base in range(2,9):
            value = self.convertToBase(value, base)
        return value
    # Method for dividing the number in the stack together and
    # returning the answer
    def division(self, base):
        reverse = Stack()
        while self.size() > 0:
            reverse.push(int(self.pop()))
        value = reverse.pop()
        while reverse.size() > 0:
            value /= reverse.pop()
        if base in range(2,9):
            value = self.convertToBase(value, base)
        return value
    # Method which creates a stack and reverses it.
    def convertToDecimal(self, number, base):
        stack = Stack()
        decimal = 0
        for n in number:
            stack.push(int(n))
        i = 0
        while stack.size() > 0:
            value = stack.pop()
            decimal += value * base ** i
            i += 1
        return str(decimal)
    # Method which converts base 10 to the given base.
    # 
    def convertToBase(self, number, base):
        power = 0
        numberpower = 0
        while numberpower <= number:
            power += 1
            numberpower = base ** power
        converted = ""
        power -= 1
        while power >= 0:
            if number < base ** power:
                converted += '0'
                power -= 1
            else:
                divisor = int(number/(base ** power))
                converted += str(divisor)
                number -= divisor * (base ** power)
                power -= 1
        return converted

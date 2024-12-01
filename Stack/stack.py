class Stack():
    def __init__(self, n):
        self.stack = []
        self.size = n
    def push(self, value):
        if len(self.stack) >= self.size:
            print("Stack Full")
        else:
            self.stack.append(value)
    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop(-1)
        else:
            print("Stack Empty")
    def top(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            print("Stack Empty")
    def display(self):
        print(self.stack)
    def length(self):
        return len(self.stack)
    def clear(self):
        self.stack = []

stack = Stack(4)
stack.push(2)
stack.push(3)
stack.push(5)
stack.push(7)
stack.push(8)
print(stack.length())
stack.display()
stack.pop()
stack.display()
stack.clear()
stack.display()
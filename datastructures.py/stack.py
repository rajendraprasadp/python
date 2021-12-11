class stack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.append(e)

    def top(self):
        if self.is_empty():
            raise "stack is empty"
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self.data.pop()

    def peek(self):
        return self.data[len(self.data)-1]


s1 = stack()
s1.push(10)
s1.push(20)
s1.push(3)
s1.push(40)
s1.push(50)
print(s1.peek())
print(s1.top())

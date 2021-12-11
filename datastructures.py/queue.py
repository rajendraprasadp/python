
class queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def display(self):
        return self.data

    def enqueue(self, e):
        self.data.append(e)

    def is_empty(self):
        return len(self.data) == 0

    def dequeue(self):
        if len(self.data) < 1:
            return None
        return self.data.pop(0)

    def first(self):
        return self.data[0]


q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)

print(q.dequeue())
print(q.dequeue())
print(q.__len__())
print(q.is_empty())
print(q.first())

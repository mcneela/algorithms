class Stack:
    def __init__(self, arr=[]):
        self.items = arr
        self.size = len(self.items)

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def push(self, item):
        self.items.append(item)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

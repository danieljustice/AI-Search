
class Stack(object):
    """This class implements all the need functions for a stack"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Returns true if stack is empty, returns false if stack has an
        item"""
        return self.items == []

    def push(self, item):
        """pushes an item onto the top of the stack"""
        self.items.append(item)

    def pop(self):
        """pops an item off of the top of the stack and returns it"""
        return self.items.pop()

    def peek(self):
        """returns the item on the top of the stack but does NOT pop it off!"""
        return self.items[len(self.items)-1]

    def size(self):
        """returns the size of the stack, how many items are in the stack"""
        return len(self.items)

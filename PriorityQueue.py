class PriorityQueue:
    def __init__(self, order=min, f=lambda x: x):
        self.items = []
        self.order = order
        self.f = f

    def enqueue(self, item):
        """Takes in an item and sorts it as a tuple in self.items with the largest item
        at index [0] and the smallest item at [len(self.items)-1]. The tuples
        are in the format (self.f(item), item)."""
        item_tuple = (self.f(item), item)
        i = 0
        while (i < len(self.items)) and (self.items[i][0] > item_tuple[0]):
            i += 1
        self.items.insert(i, item_tuple)

    def dequeue(self):
        if self.order == min:
            return self.items.pop()[1]
        else:
            return self.items.pop(0)[1]
    def peek(self):
        if self.order == min:
            return self.items[len(self.items)-1][1]
        else:
            return self.items[0][1]

    def size(self):
        return len(self.items)

    def __contains__(self, item):
        return(item == tuple[1] for tuple in self.items)

    def __getitem__(self, key):
        for (_, item) in self.items:
            if item == key:
                return item

    def __delitem__(self, key):
        i = 0
        for (_, item) in self.items:
            if item == key:
                return self.items.pop(i)
            i += 1

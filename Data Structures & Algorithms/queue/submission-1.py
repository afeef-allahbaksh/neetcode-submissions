class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self) -> bool:
        return not self.first and not self.last
        
    def append(self, value: int) -> None:
        node = Node(value)

        if self.isEmpty():
            self.first = node
            self.last = node
        else:
            self.last.next = node
            node.prev = self.last
            self.last = node
            
    def appendleft(self, value: int) -> None:
        node = Node(value)

        if self.isEmpty():
            self.first = node
            self.last = node
        else:
            node.next = self.first
            self.first.prev = node
            self.first = node
        
    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        tmp = self.last
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.last = tmp.prev
            self.last.next = None

        return tmp.val
        
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        tmp = self.first
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = tmp.next
            self.first.prev = None

        return tmp.val
        

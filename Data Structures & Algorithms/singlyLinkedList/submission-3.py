class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1) #Dummy Node
        self.tail = self.head
        
    def get(self, index: int) -> int:
        idx = 0
        current_node = self.head.next
        while current_node:
            if (idx == index):
                return current_node.val
            current_node = current_node.next
            idx += 1
    
        # Out of bounds
        return -1

    def insertHead(self, val: int) -> None:
        newHead = ListNode(val)
        newHead.next = self.head.next #Skip dummy node
        self.head.next = newHead

        # Check if the list was empty before insertion
        if self.head == self.tail:
            self.tail = newHead

        
    def insertTail(self, val: int) -> None:
        newTail = ListNode(val)
        self.tail.next = newTail
        self.tail = newTail

    def remove(self, index: int) -> bool:
        idx = 0
        current_node = self.head
        # Stop one before so we can "tie" the ends
        while current_node and idx < index:
            idx += 1
            current_node = current_node.next
        
        # Check if the node at index exists
        if current_node and current_node.next:
            # Consider if the node at index is the tail
            if current_node.next == self.tail:
                self.tail = current_node
            
            current_node.next = current_node.next.next
            return True
        
        return False

    def getValues(self) -> List[int]:
        current_node = self.head.next
        results = []
        while current_node:
            results.append(current_node.val)
            current_node = current_node.next
        return results
        

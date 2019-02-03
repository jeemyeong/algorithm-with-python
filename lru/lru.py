class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
    
    def remove(self, node):
        if not node:
            return
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            node.next.prev = None
            self.head = node.next
            node.next = None
        elif node == self.tail:
            node.prev.next = None
            self.tail = node.prev
            node.prev = None
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
    
    def items(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        return f"{[str(node) for node in self.items()]}"

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
    def __str__(self):
        return f"ListNode val: {self.value}, prev: {self.prev and self.prev.value}, next: {self.next and self.next.value}"


class LRU:
    def __init__(self, capacity):
        self.hash = {}
        self.capacity = capacity
        self.size = 0
        self.ll = DoublyLinkedList()

    def get(self, key):
        if key in self.hash:
            node = self.hash[key]
            self.ll.remove(node)
            self.ll.add(node)
            return node.value

    def put(self, key, value):
        if key in self.hash:
            node = self.hash[key]
            node.value = value
            self.ll.remove(node)
            self.ll.add(node)
        elif self.size < self.capacity:
            node = ListNode(key, value)
            self.hash[key] = node
            self.ll.add(node)
            self.size += 1
        else:
            node = ListNode(key, value)
            self.hash[key] = node
            del self.hash[self.ll.head.key]
            self.ll.remove(self.ll.head)
            self.ll.add(node)

    def __str__(self):
        return f""

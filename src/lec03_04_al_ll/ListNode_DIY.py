#tbd
#List node as well

class ListNode:
    def __init__ (self, value = 0, next = None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return f"ListNode{self.value}"

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, value):
        x = ListNode(value)
        if not self.head:
            self.head = x
        else:
            cur = self.head
            while(cur.next):
                cur = cur.next
            cur.next = x
        self.size += 1
    
    def insert(self, index, value):
        self.check_index(index)
        
        x = ListNode(value)
        if index == 0:
            self.head = x
        else:
            cur = self.head
            while(index > 1):
                cur = cur.next
                index -= 1
            
            x.next = cur.next
            cur.next =x
        self.size += 1

    def remove(self, value):

        curr = self.head
        prev = None

        while curr:
            if curr.value == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                self.size -= 1
                return True
            prev = curr
            curr = curr.next

        return False
    

    def to_list(self):
        """链表转 Python list"""
        res = []
        curr = self.head
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res

    def __repr__(self):
        return "->".join(map(str, self.to_list())) + "->None"
    
    
    def check_index(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Out of bound")
        
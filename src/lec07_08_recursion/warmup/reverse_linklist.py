class ListNode:
    def __init__ (self, val = 0, next = None):
        self.val = val
        self.next = next

def reverse_linklist(x: ListNode) -> ListNode:
    if x is None:
        return None
    
    if x.next is None:
        return x
    
    new_head = reverse_linklist(x.next)
    x.next.next = x
    #new_head.next = x  #WRONG
    x.next = None
    
    return new_head
    
   


def main():
    x1 = ListNode(1)
    x2 = ListNode(2)
    x3 = ListNode(3)
    x4 = ListNode(4)
    x5 = ListNode(5)
    x1.next = x2
    x2.next = x3
    x3.next = x4
    x4.next = x5
    
    res = reverse_linklist(x1)
    
    while res is not None:
        print(res.val)
        res = res.next
    
    
main()
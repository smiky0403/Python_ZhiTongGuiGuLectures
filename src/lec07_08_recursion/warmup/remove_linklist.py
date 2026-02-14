class ListNode:
    def __init__ (self, val = 0, next = None):
        self.val = val
        self.next = next

def remove_linklist(x: ListNode, val1: int) -> ListNode:
    if x is None:
        return None
    
    x.next = remove_linklist(x.next, val1)
    
    return x.next if x.val == val1 else x
    
   


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
    
    res = remove_linklist(x1, 3)
    
    while res is not None:
        print(res.val)
        res = res.next
    
    
main()
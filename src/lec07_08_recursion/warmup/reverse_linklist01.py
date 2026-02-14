class ListNode:
    def __init__ (self, val = 0, next = None):
        self.val = val
        self.next = next

def reverse_linklist01(head: ListNode) -> ListNode:
    def dfs(cur):
        if cur is None or cur.next is None:
            return cur
        
        nxt_head = dfs(cur.next)
        cur.next.next = cur
        cur.next = None
        
        return nxt_head
        
    res = dfs(head)
    
    return res
    
   


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
    
    res = reverse_linklist01(x1)
    
    while res is not None:
        print(res.val)
        res = res.next
    
    
main()
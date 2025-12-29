from typing import List
from ListNode_DIY import LinkedList, ListNode

def swap_pairs(my_list: List[int])-> ListNode:
    dummy = ListNode(-1)
    dummy.next = my_list.head
    
    cur = my_list.head
    prev = dummy
    while (cur and cur.next):
        nxt = cur.next
        nxxt = cur.next.next
        
        prev.next = nxt
        nxt.next = cur
        cur.next = nxxt
        
        prev = cur
        cur = nxxt
        
    return dummy.next

def main():
    my_list1 = LinkedList()
    my_list1.append(1)
    my_list1.append(2)
    my_list1.append(3)
    my_list1.append(4)
    my_list1.append(5)
    print(my_list1.to_list())
    my_list1.head = swap_pairs(my_list1)
    print(my_list1.to_list())
    
main()   
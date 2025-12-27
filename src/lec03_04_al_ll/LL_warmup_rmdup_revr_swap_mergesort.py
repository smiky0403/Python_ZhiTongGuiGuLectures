from typing import List
from ListNode_DIY import LinkedList, ListNode

def rm_dup(my_list:List[int]) -> ListNode:

    prev = my_list.head
    
    while(prev.next):
        if prev.value == prev.next.value:
            prev.next = prev.next.next
        else:
            prev = prev.next
   
    return my_list.head

def rm_dup_dist(my_list:List[int]) ->ListNode:
    dummy = ListNode(-1)
    dummy.next = my_list.head
    prev = dummy
    
    while(prev.next and prev.next.next):
        if prev.next.value == prev.next.next.value:
            last_val = prev.next.value
            while(prev.next and prev.next.value == last_val):
                prev.next = prev.next.next
        else:
            prev = prev.next

    return dummy.next

def reverse_list(my_list:List[int]) -> ListNode:
    cur = my_list.head
    if not cur:
        return None
    
    prev = None

    while(cur):
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
        
    my_list.head = cur
    return prev
        

def main():
    my_list1 = LinkedList()
    my_list1.append(1)
    my_list1.append(1)
    my_list1.append(2)
    my_list1.append(3)
    my_list1.append(3)
    print(my_list1.to_list())
    my_list1.head = rm_dup(my_list1)
    print(my_list1.to_list())
    
    my_list2 = LinkedList()
    my_list2.append(1)
    my_list2.append(1)
    my_list2.append(2)
    my_list2.append(3)
    my_list2.append(3)
    print(my_list2.to_list())
    my_list2.head = rm_dup_dist(my_list2)
    print(my_list2.to_list())   
    
    my_list3 = LinkedList()
    my_list3.append(1)
    my_list3.append(1)
    my_list3.append(2)
    my_list3.append(3)
    my_list3.append(3)
    print(my_list3.to_list())
    my_list3.head = reverse_list(my_list3)
    print(my_list3.to_list())       
    
main()

    
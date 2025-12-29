from ListNode_DIY import LinkedList, ListNode
def rm_nth(my_list: ListNode, n: int) ->ListNode:
    
    dummy = ListNode(-1)
    dummy.next = my_list
    
    slow = fast = my_list
   
    prev = dummy
    
    while n > 0:
        fast = fast.next
        n -= 1
    
    while fast:
        prev = prev.next
        slow = slow.next
        fast = fast.next
    
    prev.next = slow.next
    
    return dummy.next 

def main():
    my_list1 = LinkedList()
    my_list1.append(1)
    my_list1.append(3)
    my_list1.append(5)
    my_list1.append(7)
    my_list1.append(9)
    print(my_list1.to_list())
    my_list1.head = rm_nth(my_list1.head, 5)
    print(my_list1.to_list())

main()
from ListNode_DIY import LinkedList, ListNode

def merge_sorted_LList(my_list1: LinkedList, my_list2: LinkedList)-> ListNode:
    dummy = ListNode(-1)
    
    cur1 = my_list1.head
    cur2= my_list2.head
    
    prev = dummy
    while(cur1 and cur2):
        if cur1.value <= cur2.value:
            prev.next = cur1
            cur1 = cur1.next
        else:
            prev.next = cur2
            cur2 = cur2.next   
              
        prev = prev.next           
            
    if cur1:
        prev.next = cur1
    else:
        prev.next = cur2
  
    return dummy.next

def main():
    my_list1 = LinkedList()
    my_list1.append(1)
    my_list1.append(3)
    my_list1.append(5)
    my_list1.append(7)
    my_list1.append(9)
    print(my_list1.to_list())

    my_list2 = LinkedList()
    my_list2.append(2)
    my_list2.append(4)
    my_list2.append(5)
    my_list2.append(6)
    my_list2.append(8)
    print(my_list2.to_list())
    
    my_list_combined = LinkedList()
    my_list_combined.head = merge_sorted_LList(my_list1, my_list2 )
    print(my_list_combined.to_list())
    
main()
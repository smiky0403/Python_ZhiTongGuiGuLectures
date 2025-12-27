from ListNode_DIY import LinkedList, ListNode
def evn_odd(my_list:ListNode) ->ListNode:
    
    if not my_list or not my_list.next:
        return my_list
    
    odd = my_list
    even = even_head = odd.next

    
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        
        even.next = odd.next
        even = even.next
    
    odd.next = even_head
        
    return my_list


def main():
    my_list1 = LinkedList()
    my_list1.append(1)
    my_list1.append(2)
    my_list1.append(3)
    my_list1.append(4)
    my_list1.append(5) 
    print(my_list1.to_list())
    my_list1.head = evn_odd(my_list1.head)
    print(my_list1.to_list())

main()
from ListNode_DIY import LinkedList, ListNode
def rm_ele(my_list:ListNode, ele: int) ->ListNode:
    dummy = ListNode(-1)
    dummy.next = cur = my_list
    
    prev = dummy
    
    while cur:
        if cur.value == ele:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    
    return dummy.next

def main():
    my_list1 = LinkedList()
    my_list1.append(7)
    my_list1.append(7)
    my_list1.append(7)
    my_list1.append(4)
    my_list1.append(7)
    print(my_list1.to_list())
    my_list1.head = rm_ele(my_list1.head, 7)
    print(my_list1.to_list())

main()

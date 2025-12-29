from ListNode_DIY import LinkedList, ListNode
def add_two_ll(my_list1:ListNode, my_list2:ListNode) -> ListNode:
    cur1 = reverse_list(my_list1)
    cur2 = reverse_list(my_list2)
    carry = 0
    dummy = ListNode(-1)
    prev = dummy
    
    while(cur1 or cur2):
        if cur1 and cur2:
            cur, carry = add_2_bits(cur1.value, cur2.value, carry)
            cur1, cur2 = cur1.next, cur2.next
        elif cur1:
            cur, carry = add_2_bits(cur1.value, 0, carry)
            cur1 = cur1.next
        else:
            cur, carry = add_2_bits(cur2.value, 0, carry)
            cur2 = cur2.next
            
        prev.next = cur
        prev = prev.next
    
    if carry:
         prev.next = ListNode(1)
        
    result = reverse_list(dummy.next)        
        
    return result

def add_2_bits(val1, val2, carry):
    total = val1 + val2 + carry
    carry = int(total/10)
    rem =  total % 10
    cur = ListNode(rem)    
    return cur, carry


def reverse_list(my_list:ListNode) ->ListNode:
    prev = None
    cur = my_list
    while(cur):
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
        
    return prev

def main():
    # 987 + 65
    my_list1 = LinkedList()
    my_list1.append(9)
    my_list1.append(8)
    my_list1.append(7)
    print(my_list1.to_list())

    my_list2 = LinkedList()
    my_list2.append(6)
    my_list2.append(5)
    print(my_list2.to_list())    
    result = LinkedList()
    result.head = add_two_ll(my_list1.head, my_list2.head)
    print(result.to_list())
    print(f"Expected: {987 + 65}")
    
main()
from ListNode_DIY import ListNode, LinkedList

def get_len(my_list: LinkedList) -> int:
    cur = my_list.head
    list_len = 0
    while(cur):
        list_len += 1
        cur = cur.next
        
    return list_len

def get_kth_endnode(my_list:LinkedList, k: int) -> ListNode:
    cur1 = my_list.head
    x = ListNode(-1)
    x.next = my_list.head
    
    while(k > 0):
        if not cur1:
            return None
        cur1 = cur1.next
        k -= 1
    
    while(cur1):
        x = x.next
        cur1 = cur1.next
    
    return x.next    
        

def get_mid_node(my_list: LinkedList) ->ListNode:
    slow = fast = my_list.head
    while(fast and fast.next):
        fast = fast.next.next
        slow = slow.next
    
    return slow

def check_circle(my_list: LinkedList) ->bool:
    slow = fast = my_list.head
    while(fast and fast.next):
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    
    return False

def main():
    
    mylist1 = LinkedList()
    for i in range(10):
        mylist1.append(i)
    
    print("As list 1:", mylist1.to_list())
    
    print("List 1 has length: ", get_len(mylist1))
    print("List 1 has mid node: ", get_mid_node(mylist1))
    
    node_3rd = get_kth_endnode(mylist1, 3)
    print("Node 3rd from end: ", node_3rd)
    
    print(check_circle(mylist1))

    mylist2 = LinkedList()
    for i in range(10):
        mylist2.append(2*i)  
        
    print("As list 2:", mylist2.to_list())
    
    #add loop
    node5 = mylist2.head
    for i in range(3):
        node5 = node5.next
    #print(node5)
    node5.next = mylist2.head
    
    print(check_circle(mylist2))
    

main() 
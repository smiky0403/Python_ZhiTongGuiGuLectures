from ListNode_DIY import ListNode, LinkedList


def main():
    ll = LinkedList()

    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(ll)        # 1->2->3->None

    ll.insert(1, 10)
    print(ll)        # 1->10->2->3->None

    ll.remove(2)
    print(ll)        # 1->10->3->None

    print("As list:", ll.to_list())


if __name__ == "__main__":
    main()

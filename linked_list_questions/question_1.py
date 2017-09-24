from linked_list_questions.linked_list_impl import SinglyLinkedList


def remove_duplicates(lst):
    curr = lst.head

    while curr:
        data = curr.data
        buff = curr.next
        prev_node = curr
        while buff:
            if buff.data == data:
                prev_node.next = buff.next
                buff.next = None
                buff = prev_node.next
            else:
                prev_node = buff
                buff = buff.next
        curr = curr.next


def main():
    lst = SinglyLinkedList()
    for i in range(10):
        lst.append(i)
        lst.append(i)

    curr = lst.head
    while curr:
        print(curr.data)
        curr = curr.next

    print("edited list>>")
    remove_duplicates(lst)
    curr = lst.head
    while curr:
        print(curr.data)
        curr = curr.next


if __name__ == '__main__':
    main()

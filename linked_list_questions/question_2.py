from linked_list_questions.linked_list_impl import SinglyLinkedList


def get_kth_to_last(head, k):
    if k < 0:
        return None
    if k == 1 or k == 0:
        k = 1

    length, kth_node = _get_kth_to_last(head, k, 0, 0)
    return kth_node


def _get_kth_to_last(node, k, pos, length):
    """
    return a tuple with: length, kth_node
    """
    if node is None:
        return length, None
    else:
        length, kth_node = _get_kth_to_last(node.next, k, pos + 1, length + 1)
        if kth_node:
            return length, kth_node
        elif length - k == pos:
            kth_node = node
            return length, kth_node
        else:
            return length, None


def main():
    lst = SinglyLinkedList()
    for i in range(10):
        lst.append(i)
    print(lst.__repr__())

    head = lst.head
    kth_node = get_kth_to_last(head, -1)

    if kth_node:
        print(kth_node.data)
    else:
        print("Invalid 'k' parameter")


if __name__ == '__main__':
    main()
from linked_list_questions.linked_list_impl import SinglyLinkedList, ListNode


def partition_on_x(head, x):
  curr = head
  new_head = ListNode()
  left_list = ListNode()
  right_list = ListNode()

  while curr:
    if curr.data < x:
      if left_list.data is None:
        left_list.data = curr.data
        new_head = left_list
      else:
        left_list.next = ListNode(data=curr.data)
        left_list = left_list.next
    else:
      if right_list.data is None:
        right_list.data = curr.data
      else:
        temp = ListNode(data=curr.data, next=right_list)
        right_list = temp
    curr = curr.next
  left_list.next = right_list

  return new_head


def main():
  lst = SinglyLinkedList()
  count = 0
  for i in range(12):
    if count % 2:
      lst.append(2 * i)
    else:
      lst.append(i)
    count += 1
  print(lst.__repr__())

  head = lst.head
  new_head = partition_on_x(head, 9)
  new_lst = SinglyLinkedList(head=new_head)
  print(new_lst.__repr__())


if __name__ == '__main__':
  main()

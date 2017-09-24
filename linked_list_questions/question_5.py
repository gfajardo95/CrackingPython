from linked_list_questions.linked_list_impl import SinglyLinkedList, ListNode


def sum_lists(h1, h2):
  sum_head = ListNode()
  sum_body = None
  num_1 = h1
  num_2 = h2
  carry = 0

  while num_1 and num_2:
    curr_sum = num_1.data + num_2.data + carry
    carry = int(curr_sum / 10)
    ones = curr_sum % 10
    if sum_head.data is None:
      sum_head.data = ones
      sum_body = sum_head
    else:
      sum_body.next = ListNode(data=ones)
      sum_body = sum_body.next
    num_1 = num_1.next
    num_2 = num_2.next

  return sum_head


def main():
  num_1 = SinglyLinkedList()
  num_1.append(7)
  num_1.append(1)
  num_1.append(6)

  num_2 = SinglyLinkedList()
  num_2.append(5)
  num_2.append(9)
  num_2.append(2)

  sum_list = SinglyLinkedList(head=sum_lists(num_1.head, num_2.head))
  print(sum_list.__repr__())


if __name__ == '__main__':
  main()

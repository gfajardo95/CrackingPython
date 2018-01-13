def get_tail(node):
  curr = node
  length = 1
  
  while curr:
    if curr.next is None:
      return length, curr
    curr = curr.next
    length += 1


def is_palindrome(head):
  left = head
  length, right = get_tail(head)
  
  if length == 1:
    return True
  if length == 2:
    if left.data == right.data:
      return True
    else:
      return False
  
  mid_point = int(length / 2)
  pos = 0
  
  while pos < mid_point:
    if left.data != right.data:
      return False
    pos += 1
    left = left.next
    right = right.prev
    
  return True

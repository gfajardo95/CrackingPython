from linked_list_questions.linked_list_impl import DoublyLinkedList
from linked_list_questions.question_6 import is_palindrome


def main():
  # question 6
  list1 = DoublyLinkedList()
  list1.append(5)
  list1.append(10)
  list1.append(4)
  list1.append(6)
  
  list2 = DoublyLinkedList()
  list2.append(3)
  list2.append(6)
  list2.append(9)
  list2.append(6)
  list2.append(3)
  
  print("Question 6")
  print(is_palindrome(list1.head))
  print(is_palindrome(list2.head))
  

if __name__ == '__main__':
  main()

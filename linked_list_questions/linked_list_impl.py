class ListNode:
    """
    A node in a singly-linked list. From Dan Bader's blog
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:

    def __init__(self, head=None):
        """
        Create a new, singly-linked list. Takes O(1) time
        """
        self.head = head

    def __repr__(self):
        """
        Returns a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        """
        Insert a new element to the beginning of the list.
        Takes O(1) time.
        """
        self.head = ListNode(data=data, next = self.head)

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data)

    def find(self, key):
        """
        Find a node in the list with data matching the key.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found

    def remove(self, key):
        """
        Find the first occurence of key in the list and remove the pertaining node
        Takes O(n) time.
        """
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        if curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        """
        Reverse list in place.
        Takes O(n) time.
        """
        prev_node = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node


if __name__ == '__main__':
    pass

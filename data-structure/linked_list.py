import unittest


class Node:
    def __init__(self, item):
        self.val = item
        self.next = None


class LinkedList:
    def __init__(self, item):
        self.head = Node(item)
        self.tail = self.head

    def add(self, item):
        self.tail.next = Node(item)
        self.tail = self.tail.next

    def remove(self, item):
        if self.head.val == item:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        prev = self.head
        while prev.next.val != item:
            prev = prev.next
            if prev is None:
                print("item does not exist in linked list")
                return
        
        if prev.next == self.tail:
            prev.next = None
            self.tail = prev
        else:
            prev.next = prev.next.next        

    def reverse(self):
        self.tail = self.head
        prev = None
        cur = self.head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def printlist(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next


class TestLinkedList(unittest.TestCase):
    def test(self):
        ll = LinkedList(3)
        self.assertEqual(ll.head.val, 3)
        ll.add(4)
        self.assertEqual(ll.head.next.val, 4)
        ll.add(5)
        self.assertEqual(ll.head.next.next.val, 5)
        ll.remove(3)
        self.assertEqual(ll.head.val, 4)
        ll.remove(4)
        self.assertEqual(ll.head.val, 5)
        ll.add(6)
        self.assertEqual(ll.head.next.val, 6)
        ll.add(7)
        self.assertEqual(ll.head.next.next.val, 7)
        ll.printlist()
        ll.remove(6)
        self.assertEqual(ll.head.next.val, 7)

        ll2 = LinkedList(9)
        ll2.add(8)
        ll2.add(7)
        ll2.reverse()
        self.assertEqual(ll2.head.val, 7)
        self.assertEqual(ll2.head.next.val, 8)


if __name__ == '__main__':
    unittest.main()

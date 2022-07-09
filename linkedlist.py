class Node:

    def __init__(self, value = 0, next_node = None):
        self.value = value
        self.next_node = next_node


class LinkedList:

    def __init__(self, value: int, next_node: Node):
        self.head = Node(value, next_node)

    def insertAtHead(self, value: int) -> None:
        previous_head = self.head
        current_head = Node(value, previous_head)
        self.head = current_head
        return None

    def insertAtTail(self, value: int) -> None:
        current_node = self.head
        while current_node.next_node != None:
            current_node = current_node.next_node
        current_node.next_node = Node(value, None)
        return None

    def printLinkedList(self) -> None:
        current_node = self.head
        while current_node != None:
            print(current_node.value, "---->", end = " ")
            current_node = current_node.next_node
        print(None)
        return None


linkedlist1 = LinkedList(1, None)

linkedlist1.printLinkedList()
linkedlist1.insertAtHead(0)
linkedlist1.insertAtTail(2)
linkedlist1.printLinkedList()













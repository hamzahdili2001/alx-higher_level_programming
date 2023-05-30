#!/usr/bin/python3
"""singly linked list Node"""


class Node:
    """define singly linked list"""
    def __init__(self, data, nextNode=None):
        """constractor
        Args:
            data - data of the the Node
            nextNode - next Node address"""
        self.data = data
        self.nextNode = nextNode

    @property
    def data(self):
        """Returns: data"""
        return self._data

    @data.setter
    def data(self, value):
        """set the nodes
        Args:
            value - value of the data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def nextNode(self):
        """Returns: next Node"""
        return self._nextNode

    @nextNode.setter
    def nextNode(self, value):
        """sets the next Node
        Args:
            value - next node value."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._nextNode = value


"""singly linked list"""


class SinglyLinkedList:
    """singly linked linked"""
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """Inserting node in sorted mode
        Args: value - value -> data"""
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return

        if value < self.head.data:
            newNode.nextNode = self.head
            self.head = newNode
            return

        current = self.head
        while current.nextNode is not None and current.nextNode.data < value:
            current = current.nextNode
        newNode.nextNode = current.nextNode
        current.nextNode = newNode

    def __str__(self):
        """get nodes"""
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.nextNode
        return "\n".join(nodes)

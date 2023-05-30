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
        return self.__data

    @data.setter
    def data(self, value):
        """set the nodes
        Args:
            value - value of the data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def nextNode(self):
        """Returns: next Node"""
        return self.__nextNode

    @nextNode.setter
    def nextNode(self, value):
        """sets the next Node
        Args:
            value - next node value."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__nextNode = value


class SinglyLinkedList:
    """singly linked linked"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Inserting node in sorted mode
        Args: value - value -> data"""
        newNode = Node(value)
        if self.__head is None:
            self.__head = newNode
        elif value < self.__head.data:
            newNode.nextNode = self.__head
            self.__head = newNode
        else:
            current = self.__head
            while current.nextNode is not None and current.nextNode.data < value:
                current = current.nextNode
            newNode.nextNode = current.nextNode
            current.nextNode = newNode

    def __str__(self):
        """get nodes"""
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.nextNode
        return "\n".join(nodes)

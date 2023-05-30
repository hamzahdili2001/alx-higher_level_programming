#!/usr/bin/python3
"""singly linked list Node"""


class Node:
    """define singly linked list"""
    def __init__(self, data, next_node=None):
        """constractor
        Args:
            data - data of the the Node
            nextNode - next Node address"""
        self.data = data
        self.next_node = next_node

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
    def next_node(self):
        """Returns: next Node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the next Node
        Args:
            value - next node value."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """singly linked linked"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Inserting node in sorted mode
        Args: value - value -> data"""
        newNode = Node(value)

        if self.__head is None:
            newNode.next_node = None
            self.__head = newNode
        elif self.__head.data > value:
            newNode.next_node = self.__head
            self.__head = newNode
        else:
            current = self.__head
            while current.next_node is not None and\
                    current.next_node.data < value:
                current = current.next_node
            newNode.next_node = current.next_node
            current.next_node = newNode

    def __str__(self):
        """get the node and join them in nodes"""
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

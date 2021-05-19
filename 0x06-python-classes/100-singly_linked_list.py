#!/usr/bin/python3
"""Define class for node and class for singly linked list"""


class Node:
    """Represent a node"""

    def __init__(self, data, next_node=None):
        """Initialize node.

        Args:
        data (int): The data of the new Node.
        next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve data"""
        return(self.__data)

    @data.setter
    def data(self, value):
        """Set value of data"""
        if type(value) is not int:
            raise Typerror("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """"Retrieve next_node"""
        return(self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Represent Singly linked list"""

    def __init__(self):
        """Initialize singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the
        list (increasing order)

        Args:
        value (Node): The new Node to insert.
        """

        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """for print singly lnked list"""
        val = []
        tmp = self.__head
        while tmp is not None:
            val.append(str(tmp.data))
            tmp = tmp.next_node
        return('\n'.join(val))

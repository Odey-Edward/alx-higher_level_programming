#!/usr/bin/python3
""" defines a node of a singly linked list """

class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


    @property
    def data(self):
        ''' retrieve data '''
        return (self.__data)


    @data.setter
    def data(self, value):
        ''' set the data '''
        if type(value) != int:
            raise TypeError("data must be an integer")

        self.__data = value


    @property
    def next_node(self):
        ''' retrieve next node '''
        return (self.__next_node)


    @next_node.setter
    def next_node(self, value):
        ''' set the next node '''
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    ''' defines a singly linked list '''

    def __init__(self):
        self.__head = None


    def sorted_insert(self, value):
        new = Node(value)

        if self.__head is None:
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node and tmp.next_node.data < value:
                tmp = tmp.next_node

            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))


sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)

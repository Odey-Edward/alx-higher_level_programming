#!/usr/bin/python3
""" defines a node of a singly linked list """


class Node:
    '''Defining the Node Class'''

    def __init__(self, data, next_node=None):
        '''Initializes attributes for the Node class
        Args:
            data (int): value to assign to the data attribute
            next_node (Node): reference to the next node of a singly
            linked list
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        ''' retrieve data '''
        return (self.__data)

    @data.setter
    def data(self, value):
        ''' set the data of a node
        Args:
            value (int): the value assigned to the data attribute
        '''
        if type(value) != int:
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        ''' retrieve next node '''
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        ''' set the next node
        Args:
            value (Node): the next Node Object
        '''
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    ''' defines a singly linked list '''

    def __init__(self):
        ''' The singlyLinkedList initialization method '''
        self.__head = None

    def sorted_insert(self, value):
        '''method for insecting element in a linked list in
        a sorted order

        Args:
            value (int): data assigned to the new node
        '''
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
        '''This method defines how the class is represented when
        printed'''
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))

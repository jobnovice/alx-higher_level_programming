#!/usr/bin/python3
'''Class Node is defined'''


class Node:
    ''' yeah class node defined in it'''
    def __init__(self, data, next_node=None):
        '''the default constructor
            Args:
                data (int): an integer valued data
                next_node (node): the next node in the singly-linked list
            Returns:
                none'''
        self.__data = data
        self.__next_node = None
    
    @property
    def data(self):
        ''' to retrieve the information
            Returns:
                the data'''
        return self.__data
    
    @data.setter
    def data(self, value):
        ''' to set the value 
            Args:
                value (int): to set the value in the data
            Returns:
                None'''
        if type (value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        ''' Returns: the value of the next node'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''to set the value of the next node
            Args:
                value (node):insert the next node
            Returns:
                None'''
        if type(value) is not Node or value != None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
    
    def __str__(self):
        """String representation of Node instance
        Returns:
            Formatted string representing the node
        """
        return str(self.__data)

class SinglyLinkedList:
    ''' new class singly linked list defined'''

    
    def __init__(self):
        '''intilalizes the node on the data itself
            Returns:
                None'''
        self.__head = None
    def sorted_insert(self, value):
        """ inserts a new Node instance into the correct sorted position
        Args:
            value (int): data stored inside the new node
        Returns:
            None
        """
        new = Node(value)
        tmp = self.__head
        if tmp is None or tmp.data >= value:
            if tmp:
                new.next_node = tmp
            self.__head = new
            return
        while tmp.next_node is not None:
            if tmp.next_node.data >= value:
                break
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new

    def __str__(self):
        """String representation of SinglyLinkedList instance
        Returns:
            Formatted string representing the linked list
        """
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp)
            if tmp.next_node is not None:
                string += "\n"
            tmp = tmp.next_node
        return string
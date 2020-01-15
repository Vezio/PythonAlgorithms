#!/usr/bin/env python3
# Author: Tyler Rimaldi

from .Node import Node

class LinkedList:
    """A list of linked nodes in forming a linear chain"""
    def __init__(self):
        self.__head = None
        self.__tail = None

    def add_to_front(self, data):
        """Add a new node to the front of the list"""
        new_node = Node(data, None) 
        if self.__head == None:
            self.__head = new_node
            self.__tail = new_node
        else:
            old_head = self.__head
            self.__head = new_node
            self.__head.set_next(old_head)

    def add_to_back(self, data):
        """Add a new node to the back of the list"""
        new_node = Node(data, None) 
        if self.__head == None:
            self.__head = new_node
            self.__tail = new_node
        else:
            old_tail = self.__tail
            self.__tail = new_node
            old_tail.set_next(self.__tail)

    def remove_from_front(self):
        """Remove a node from the front of the list"""
        if self.is_list_empty() is False: 
            if self.__head.get_next() is not None:
                old_head = self.__head
                self.__head = self.__head.get_next()
                return old_head.get_data()
            else: 
                old_head = self.__head
                self.__head = None
                return old_head.get_data()
        else:
            return "Empty"

    def remove_from_back(self):
        """Remove a node from the back of the list"""
        if self.__tail is not None:
            if self.__tail == self.__head:
                old_tail = self.__tail
                self.__tail = None
                self.__head = None
                return old_tail.get_data()
            else:
                current = self.__head
                # Find the last node in the list
                while current.get_next() is not None:
                    self.__tail = current
                    old_tail = current
                    current = current.get_next()
                # Kill the last node
                self.__tail.set_next(None)
                return old_tail.get_data()
        else: 
            return "Empty"

    def get_head(self):
        """Get the head of the list"""
        return self.__head

    def get_tail(self):
        """Get the tail of the list"""
        return self.__tail

    def is_list_empty(self):
        """Check if the list is empty"""
        if self.__head is None:
            return True 
        else:
            return False

    def clear_list(self):
        """Clear the entire list, reset the head and tail"""
        self.__head = None
        self.__tail = None

    def print_list(self):
        """Print out the entire list data contents"""
        if self.is_list_empty() is False:
            current = self.__head
            while current is not None:
                print(current.get_data())
                current = current.get_next()
            
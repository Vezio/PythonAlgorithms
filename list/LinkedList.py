#!/usr/bin/env python3
# Author: Tyler Rimaldi

from .Node import Node

class LinkedList:
    """A list of linked nodes in forming a linear chain"""
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, data):
        """Add a new node to the front of the list"""
        new_node = Node(data,None) 
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            old_head = self.head
            self.head = new_node
            self.head.set_next(old_head)

    def add_to_back(self, data):
        """Add a new node to the back of the list"""
        new_node = Node(data,None) 
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            old_tail = self.tail
            self.tail = new_node
            old_tail.set_next(self.tail)

    def remove_from_front(self):
        """Remove a node from the front of the list"""
        if self.is_list_empty() is False: 
            if self.head.get_next() is not None:
                old_head = self.head
                self.head = self.head.get_next()
                return old_head.data
            else: 
                old_head = self.head
                self.head = None
                return old_head.data
        else:
            return "Empty"

    def remove_from_back(self):
        """Remove a node from the back of the list"""
        if self.tail is not None:
            if self.tail == self.head:
                old_tail = self.tail
                self.tail = None
                self.head = None
                return old_tail.data
            else:
                current = self.head
                # Find the last node in the list
                while current.get_next() is not None:
                    self.tail = current
                    old_tail = current
                    current = current.get_next()
                # Kill the last node
                self.tail.set_next(None)
                return old_tail.data
        else: 
            return "Empty"

    def get_head(self):
        """Get the head of the list"""
        return self.head

    def get_tail(self):
        """Get the tail of the list"""
        return self.tail

    def is_list_empty(self):
        """Check if the list is empty"""
        if self.head is None:
            return True 
        else:
            return False

    def clear_list(self):
        """Clear the entire list, reset the head and tail"""
        self.head = None
        self.tail = None

    def print_list(self):
        """Print out the entire list data contents"""
        if self.is_list_empty() is False:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.get_next()
            
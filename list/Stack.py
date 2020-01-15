#!/usr/bin/env python3
# Author: Tyler Rimaldi

from .LinkedList import LinkedList

class Stack:
    """Stack LIFO"""
    def __init__(self):
        self.__s = LinkedList()

    def push(self, data):
        self.__s.add_to_front(data)

    def pop(self):
        return self.__s.remove_from_front()    

    def get_head(self):
        return self.__s.get_head()

    def get_tail(self):
        return self.__s.get_tail()

    def clear_stack(self):
        self.__s.clear_list()

    def is_stack_empty(self):
        return self.__s.is_list_empty()    

    def print_stack(self):
        self.__s.print_list()
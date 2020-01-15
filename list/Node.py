#!/usr/bin/env python3
# Author: Tyler Rimaldi

class Node:
    """Node--an object containing data and a pointer to the next node."""
    def __init__(self, data, next_node):
        self.__data = data
        self.__next = next_node
    
    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, data):
        self.__data = data
    
    def set_next(self, node):
        self.__next = node 

#!/usr/bin/env python3
# Author: Tyler Rimaldi

class Node:
    """Node--an object containing data and a pointer to the next node."""
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node
        
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data
    
    def set_next(self, node):
        self.next = node 

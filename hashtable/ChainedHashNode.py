#!/usr/bin/env python3
# Author: Tyler Rimaldi

class ChainedHashNode:
    """Chainable node that will sit on the hashtable"""
    def __init__(self, key = 0, data = 0, next_node = None):
        """Optionally parameterized constructor"""
        self.__key  = key
        self.__data = data
        self.__next = next_node

    def get
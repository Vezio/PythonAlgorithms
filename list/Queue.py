#!/usr/bin/env python3
# Author: Tyler Rimaldi

from .LinkedList import LinkedList

class Queue:
    """Queue FIFO"""
    def __init__(self):
        self.__q = LinkedList()

    def enqueue(self, data):
        self.__q.add_to_back(data)

    def dequeue(self):
        return self.__q.remove_from_front()    

    def get_head(self):
        return self.__q.get_head()
    
    def get_tail(self):
        return self.__q.get_tail()

    def clear_queue(self):
        self.__q.clear_list()

    def is_queue_empty(self):
        return self.__q.is_list_empty()    

    def print_queue(self):
        self.__q.print_list()
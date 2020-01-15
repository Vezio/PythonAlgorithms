#!/usr/bin/env python3
# Author: Tyler Rimaldi

from list import Stack
from list import Queue

def run_lists():
    """Demo the list data structures"""
    queue = Queue.Queue()
    stack = Stack.Stack()
    print("Queue: ")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.print_queue()
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())  
    print("Stack: ")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.print_stack()
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

if __name__ == "__main__":
    run_lists()

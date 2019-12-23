import node

class LinkedList:
    """A list of linked nodes in forming a linear chain"""
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self,data):
        """Add a new node to the front of the list"""
        new_node = node.Node(data,None) 
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            old_head = self.head
            self.head = new_node
            self.head.set_next(old_head)

    def enqueue(self, data):
        """Add a new node to the back of the list"""
        new_node = node.Node(data,None) 
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            old_tail = self.tail
            self.tail = new_node
            old_tail.set_next(self.tail)

    def pop(self):
        """Remove a node from the front of the list"""
        if self.head.get_next() is not None:
            self.head = self.head.get_next()

    def dequeue(self):
        """Remove a node from the back of the list"""
        if self.tail is not None:
            if self.tail == self.head:
                self.tail = None
                self.head = None
            else:
                current = self.head
                # Find the last node in the list
                while not current.get_next() == None:
                    self.tail = current
                    current = current.get_next()
                # Kill the last node
                self.tail.set_next(None)

    def print_list(self):
        """Print out the entire list data contents"""
        current = self.head
        if current is not None:
            while not current == None:
                print(current.data)
                current = current.get_next()
        else:
            print("Empty List.")

            import linkedlist


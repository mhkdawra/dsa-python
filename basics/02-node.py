'''
A node is a basic building block of a data structure.
It consists of two parts: One to store value and a next pointer or a object reference pointer
The next pointer points to the next object/node
[3|next]->[5|next]->[7|null]
Node_1 has value 3 and it's next pointer points to Node_2 with 5 as value and so on
Node_3 has next pointer null, so that's the end of the list
'''

class Node:
    '''
    A class to represent Node
    '''
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return '{0}-->{1}'.format(self.value, self.next)

def print_next(node):
    print(node.value)
    print()
    if node.next:
        print_next(node.next)
    else:
        print('End')

if __name__ == "__main__":
    node_1 = Node(3)
    node_2 = Node(5)
    node_3 = Node(7)
    node_1.next = node_2
    node_2.next = node_3
    print(node_1)
    print(node_2)
    print(node_3)
    print()
    print_next(node_1)

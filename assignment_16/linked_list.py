
class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self, head):
        self.head = Node(head, None)
    
    def print_data(self):
        ref_node = self.head
        while ref_node.next != None:
            print(ref_node.data)
            ref_node = ref_node.next
        print(ref_node.data)
    
    def length(self):
        ref_node = self.head
        counter = 0
        while ref_node.next != None:
            counter += 1
            ref_node = ref_node.next
        counter += 1
        return counter
    
    def append(self, next_node):
        ref_node = self.head
        while ref_node.next != None:
            ref_node = ref_node.next
        ref_node.next = Node(next_node, None)

print("Testing class 'Node()'...")
A = Node(4, None)
assert A.data == 4
assert A.next == None
B = Node(8, None)
A.next = B
assert A.next.data == 8
print("PASSED")
print("\n")

print("Testing class 'LinkedList()'...")
linked_list = LinkedList(4)
assert linked_list.head.data == 4
linked_list.append(8)
assert linked_list.head.next.data == 8
linked_list.append(9)
linked_list.print_data()
assert linked_list.length() == 3
print("PASSED")

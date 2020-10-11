
class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next
        self.index = 0

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
        index_counter = 0
        while ref_node.next != None:
            ref_node = ref_node.next
            index_counter += 1
        ref_node.next = Node(next_node, None)
        ref_node.next.index = index_counter + 1
    
    def push(self, new_data):
        ref_node = self.head
        self.head = Node(new_data, None)
        while ref_node.next != None:
            self.append(ref_node.data)
            ref_node = ref_node.next
        self.append(ref_node.data)
    
    def get_node(self, index):
        ref_node = self.head
        for i in range(index):
            ref_node = ref_node.next
        return ref_node.data

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
print("\n")

print("Testing methods 'length' and 'push'...")
linked_list = LinkedList('b')
linked_list.append('e')
linked_list.append('f')
linked_list.push('a')
assert linked_list.length() == 4
print("PASSED")
print("Testing attribute 'index'...")
assert linked_list.head.index == 0
assert linked_list.head.next.index == 1
assert linked_list.head.next.next.index == 2
assert linked_list.head.next.next.next.index == 3
print("PASSED")
print("Testing method 'get_node'...")
assert linked_list.get_node(0) == 'a'
assert linked_list.get_node(1) == 'b'
assert linked_list.get_node(2) == 'e'
assert linked_list.get_node(3) == 'f'
print("PASSED")

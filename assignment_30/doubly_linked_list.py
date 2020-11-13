class Node():
    def __init__(self, prev, data, next):
        self.prev = prev
        self.data = data
        self.next = next
        self.index = 0

class DoublyLinkedList():
    def __init__(self, head):
        self.head = Node(None, head, None)
    
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
        ref_node.next = Node(ref_node, next_node, None)
        ref_node.next.index = index_counter + 1
    
    def push(self, new_data):
        ref_node = self.head
        self.head = Node(None, new_data, None)
        while ref_node.next != None:
            self.append(ref_node.data)
            ref_node = ref_node.next
        self.append(ref_node.data)
    
    def get_node(self, index):
        ref_node = self.head
        for i in range(index):
            ref_node = ref_node.next
        return ref_node
    
    def delete(self, index):
        ref_node = self.head
        for i in range(index):
            ref_node = ref_node.next
        for i in range(index, self.length() - 1):
            ref_node.data = ref_node.next.data
            if ref_node.index == self.length() - 2:
                ref_node.next = None
            ref_node = ref_node.next
    
    def insert(self, new_data, index):
        ref_node = self.head
        for i in range(index):
            ref_node = ref_node.next
        for i in range(index, self.length() - 1):
            value = ref_node.data
            next_value = ref_node.next.data
            if i == index:
                ref_node.data = new_data
            ref_node.next.data = value
            ref_node = ref_node.next
        self.append(next_value)

doubly_linked_list = DoublyLinkedList('a')
doubly_linked_list.append('c')
doubly_linked_list.append('d')
doubly_linked_list.append('e')
doubly_linked_list.insert('b',1)
doubly_linked_list.delete(3)
current_node = doubly_linked_list.get_node(3)
node_values = [current_node.data]
for _ in range(3):
    current_node = current_node.prev
    node_values.append(current_node.data)
print(node_values)

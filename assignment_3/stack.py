class Stack():
    def __init__(self):
        self.data = []
    
    def push(self, push_value):
        self.data.append(push_value)
    
    def pop(self):
        self.data.remove(self.data[-1])
    
    def peek(self):
        return self.data[-1]

s = Stack()
print("Asserting Stack() was initialized ...")
assert s.data == [], "didn't work"
s.push('a')
s.push('b')
s.push('c')
print("Asserting that s.push() works ...")
assert s.data == ['a', 'b', 'c'], "doesn't work"
s.pop()
print("Asserting that s.pop() works ...")
assert s.data == ['a', 'b'], "doesn't work"
print("Asserting that s.peek() works ...")
assert s.peek() == 'b', "didn't work"
print("Asserting that s.peek() didn't change s.data ...")
assert s.data == ['a', 'b'], "s.peek() changed s.data"
print("ALL PASSED")

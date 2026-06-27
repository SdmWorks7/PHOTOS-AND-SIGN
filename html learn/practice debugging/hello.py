import pytest

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.peek())
# print(stack.pop())
# print(stack.size())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())



def test_push_and_size():
    stack = Stack()
    stack.push(1)
    assert stack.size() == 1
def test_pop():
    stack = Stack()
    stack.push(1)
    assert stack.pop() == 1
def test_peek():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1
def test_is_empty():
    stack = Stack()
    stack.push(1)
    assert stack.is_empty() == False
def test_pop_empty():
    with pytest.raises(ValueError):
        stack = Stack()
        stack.pop()
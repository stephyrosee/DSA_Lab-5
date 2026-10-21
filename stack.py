# stack.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None


def infix_to_postfix(expression):
    """
    Converts an infix expression to postfix (Reverse Polish Notation)
    using the Stack class, strictly observing operator precedence and 
    left-to-right associativity for operators like * and /.
    """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    ops = Stack()
    output = []

    tokens = expression.replace(" ", "")

    for token in tokens:
        if token.isalnum():
            output.append(token)
        elif token == '(':
            ops.push(token)
        elif token == ')':
            while not ops.is_empty() and ops.peek() != '(':
                output.append(ops.pop())
            ops.pop()  
        elif token in precedence:
            while not ops.is_empty() and ops.peek() != '(' and precedence[ops.peek()] >= precedence[token]:
          
                if token != '^' and precedence[ops.peek()] == precedence[token]:
                    break
                output.append(ops.pop())
            ops.push(token)

    while not ops.is_empty():
        output.append(ops.pop())

    return " ".join(output)
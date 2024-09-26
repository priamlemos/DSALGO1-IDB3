Q = []

Q.append(5)
Q.append(3)
print("The Length is: ")
print(len(Q))
print("The return value of pop is " )
print(Q.pop())
#isEmpty
print("Is the stack empty?")
if len(Q) == 0:
    print("True")
else:
    print("False")
print("The return value of pop is " )
print(Q.pop())
#isEmpty
print("Is the stack empty?")
if len(Q) == 0:
    print("True")
else:
    print("False")
Q.append(7)
Q.append(9)
#Top()
x = len(Q)
element = (Q)[x - 1]
print("The Top of the stack is: ")
print(element)
Q.append(4)
print("The length of the stack is: ")
print(len(Q))
print("The return value of pop is "  )
print(Q.pop())
Q.append(6)
Q.append(8)
Q.pop()
print(Q)
print()

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
            return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

x = Stack()

x.push(5)
x.push(3)
print(x.pop())
x.push(2)
x.push(8)
print(x.pop())
print(x.pop())
x.push(9)
x.push(1)
print(x.pop())
x.push(7)
x.push(6)
print(x.pop())
print(x.pop())
x.push(4)
print(x.pop())
print(x.pop())

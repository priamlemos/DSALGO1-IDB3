class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue)<1:
            return None
        return self.queue.pop(0)

    def display(self):
        return self.queue

    def len(self):

        return len(self.queue)

    def empty(self):
        if len(self.queue) == 0:
            return "true"
        else:
            return "false"
    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            return self.queue.index[2]

Q = Queue()
Q.enqueue(5)
Q.enqueue(3)
print("Length of queue is ", Q.len())
print("The element that remove is: ", Q.dequeue())
print("The element that remove is: ", Q.dequeue())
print("Is stack is empty? ", Q.empty())
print("The element that remove is: ", Q.dequeue())
Q.enqueue(7)
Q.enqueue(9)
print(Q.queue)
print("The first element in queue is: ", Q.queue[0])
Q.enqueue(4)
print("The length of queue is ", Q.len())
print("The element that remove is: ", Q.dequeue())
print(Q.queue)

print()

X = Queue()
print("The return values are: ")
X.enqueue(5)
X.enqueue(3)
print(X.dequeue())
X.enqueue(2)
X.enqueue(8)
print(X.dequeue())
print(X.dequeue())
X.enqueue(9)
X.enqueue(1)
print(X.dequeue())
X.enqueue(7)
X.enqueue(6)
print(X.dequeue())
print(X.dequeue())
X.enqueue(4)
print(X.dequeue())
print(X.dequeue())

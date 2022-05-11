class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element);

    def pop(self):
        if (len(self.stack) == 0):
            print("error: stack is empty, there is no element to pop")
            return
        result = self.stack[len(self.stack)-1]
        self.stack.pop()

        return result

    def top(self):
        if (len(self.stack) == 0):
            print("error: stack is empty, there is no element to return")
            return
        result = self.stack[len(self.stack)-1]
        return result

    def isEmpty(self):
        return (len(self.stack) == 0)

    def size(self):
        return (len(self.stack))

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if (len(self.queue) == 0):
            print("queue is empty, nothing to return")
            return
        result = self.queue[0]
        self.queue.remove(result)
        return result

    def rear(self):
        if (len(self.queue) == 0):
            print("queue is empty, nothing to return")
            return
        return (self.queue[len(self.queue) - 1])

    def front(self):
        if (len(self.queue) == 0):
            print("queue is empty, nothing to return")
            return
        return (self.queue[0])

    def size(self):
        return (len(self.queue))

    def isEmpty(self):
        return (len(self.queue) == 0)

def main():
    myStack = Stack()
    myStack.push(42)
    myStack.push(42)
    myStack.push(42)
    myStack.push(42)

    print(myStack.size())
    myStack.pop()
    print(myStack.size())
    myStack.pop()
    myStack.top()

    myQueue = Queue()
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.enqueue(3)
    print ("Size of queue: ", myQueue.size())
    print(myQueue.dequeue())


if __name__ == '__main__':
    main()
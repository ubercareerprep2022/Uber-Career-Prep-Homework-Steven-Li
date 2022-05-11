class Node:
    def __init__(self, element):
        self.element = element
        self.pointer = None

class LinkedList:
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def push(self, node):
        #if the first node
        if (self.front == None):
            self.front = node
            self.back = node

        else:
            (self.back).pointer = node
            self.back = node

        self.length += 1

    def pop(self):
        # if the first node
        if (self.front == None):
            print("list is empty")
            return
        else:
            if (self.length == 1):
                result = self.front.element
                self.front = None
                self.back = None
                self.length = 0
                return result
            #traversing list to find the node that points to the last one
            result = self.back
            start = self.front

            while (start.pointer != result):
                start = start.pointer

            self.back = start
            (self.back).pointer = None
            self.length -= 1
            return result.element

    def insert(self, index, node):

        if (index > self.length):
            return

        if (index == 1):
            current_node = self.front
            node.pointer = current_node
            self.front = node

            self.length += 1
            return

        if (index == self.length):
            self.push(node)
            return

        count = 2
        current_node = self.front
        while (count != index):
            current_node = current_node.pointer
            count += 1
        temp = current_node.pointer
        current_node.pointer = node
        node.pointer = temp
        self.length += 1

    def elementAt(self, index):
        if index > self.length:
            return None
        count = 1
        result = self.front
        while (count != index):
            result = result.pointer
            count += 1

        return result.element

    def size(self):
        return self.length

    def printList(self):
        result = ''
        front = self.front
        while (front != None):
            result = result + str(front.element)
            front = front.pointer

        return result

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



def iterative_reverse(list):
    myList = LinkedList()

    node_array = []
    front = list.front

    while (front != None):
        node_array.append(front)
        front = front.pointer

    for node in reversed(node_array):
        node.pointer = None
        myList.push(node)

    return myList

def stack_reverse(list):
    myStack = Stack()
    myList = LinkedList()

    front = list.front

    while (front != None):
        myStack.push(front)
        front = front.pointer

    while (myStack.isEmpty() == False):
        node = myStack.pop()
        node.pointer = None
        myList.push(node)

    return myList

def recursive_reverse(list):
    myList = LinkedList()

    def recursive_function(node):
        if ((list.front).pointer == None):
            myList.push(list.front)
            return
        else:
            recursive_function((list.front).pointer)

    recursive_function(list.front)
    return myList





if __name__ == "__main__":
    myList = LinkedList()
    four = Node(4)
    three = Node(3)
    two = Node(2)
    one = Node(1)

    myList.push(four)
    myList.push(three)
    myList.push(two)
    myList.push(one)

    print(myList.printList())

    rev_list = iterative_reverse(myList)
    print(rev_list.printList())

    myList = LinkedList()
    four = Node(4)
    three = Node(3)
    two = Node(2)
    one = Node(1)

    myList.push(four)
    myList.push(three)
    myList.push(two)
    myList.push(one)
    recur_list = recursive_reverse(myList)
    print(recur_list.printList())

    stack_list = stack_reverse(myList)
    print(stack_list.printList())


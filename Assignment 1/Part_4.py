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
        back = None
        while (front != None):
            result = result + str(front.element)
            front = front.pointer

        return result



four = Node(4)
three = Node(3)
two = Node(2)
one = Node(1)
onev = Node(1)

myList = LinkedList()
print("length: ", myList.length)
print(myList.printList())
myList.push(four)
print("length: ", myList.length)
print(myList.printList())
myList.push(three)
print("length: ", myList.length)
print(myList.printList())
myList.push(two)
print("length: ", myList.length)
print(myList.printList())
myList.push(one)
print("length: ", myList.length)
myList.insert(2, onev)
print("length: ", myList.length)



print(myList.printList())
#myList.insert(1, three) #insert is broken still

print(myList.elementAt(1))
print(myList.elementAt(2))
print(myList.elementAt(3))
print(myList.elementAt(4))
print(myList.elementAt(5))

print(myList.pop())

print(myList.pop())

print(myList.pop())

print(myList.pop())

print(myList.pop())




#print(myList.pop())




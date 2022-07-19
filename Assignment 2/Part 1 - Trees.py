
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

bleft = Node(3)
bright = Node(6)
uleft = Node(7)
uright = Node(17, bleft, bright)
top = Node(1, uleft, uright)

"""
Implement a method called print() to print the values of the data in all the TreeNodes in a Tree above. 
For example, running print() on the Tree above should produce one of the three values below:

1 7 17 6 3
7 1 6 17 3
7 6 3 17 1 

"""
def print_tree(root):
    if (root == None):
        return
    else:
        print_tree(root.left)
        print(root.data)
        print_tree(root.right)

print_tree(top)

"""
Implement a method called printLevelByLevel() for the class OrganizationStructure that prints it level by level.
For example, running printLevelByLevel() on the OrganizationStructure above should produce the following output:

Name: A, Title: CEO

Name: B, Title: CFO
Name: C, Title: CTO

Name: I, Title: Director
Name: D, Title: Manager
Name: E, Title: Manager

Name: J, Title: Sales Representative
Name: F, Title: Engineer
Name: G, Title: Engineer
Name: H, Title: Engineer

Name: K, Title: Sales Intern
"""

class Organization:
    def __init__(self, CEO=None):
        self.CEO = CEO

class Employee:
    def __init__(self, name=None, title=None, list = None):
        self.name = name
        self.title = title
        self.list = list

"""Did not want to reconstruct the entire tree manually"""
salesIntern = Employee('K', 'Sales Intern')
salesRep = Employee('J', 'Sales Representative', [salesIntern])
director = Employee('I', 'Director', [salesRep])
cfo = Employee('B', 'CFO', [director])
engineerF = Employee('F', 'Engineer')
engineerG = Employee('G', 'Engineer')
engineerH = Employee('H', 'Engineer')
managerD = Employee('D', 'Manager', [engineerF, engineerG, engineerH])
managerE = Employee('E', 'Manager')
cto = Employee('C', 'CTO', [managerD, managerE])
ceo = Employee('A', 'CEO', [cfo, cto])
org = Organization(ceo)

def printLevelByLevel(root):
    current_level = []
    current_level.append(root.CEO)
    next_level = []

    while (len(current_level) != 0):
        current_node = current_level.pop()
        print("Name: ", current_node.name, ", Title: ", current_node.title)

        if(current_node.list != None):
            for employee in current_node.list:
                next_level.append(employee)

        if (len(current_level) == 0):
            current_level = next_level
            next_level = []
            print(" ")

printLevelByLevel(org)
"""
[Trees - Ex3] Exercise: Printing the number of levels
Implement a method called for the class OrganizationStructure that prints the number of levels in it. 
For example, running printNumLevels() on the OrganizationStructure above should print 5. 
Running printNumLevels() on the OrganizationStructure below should print 4.
"""

def printNumLevels(root):
    current_level = []
    current_level.append(root.CEO)
    next_level = []
    count = 0

    while (len(current_level) != 0):
        current_node = current_level.pop()

        if(current_node.list != None):
            for employee in current_node.list:
                next_level.append(employee)

        if (len(current_level) == 0):
            current_level = next_level
            next_level = []
            count = count + 1

    print("Number of Levels: ", count)

printNumLevels(org)

def find(root, target):

    if (root == None):
        return False

    if (root.data == target):
        print("Found")
        return True

    if (root.data > target):
        return find(root.right, target)
    else:
        return find(root.left, target)

find(top, 17)

"""
IMPLEMENT INSERT
"""



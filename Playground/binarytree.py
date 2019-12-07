# A Python class that represents an individual node  
# in a Binary Tree 
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.val):
            if(node.left != None):
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if(node.right != None):
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.val):
            return node
        elif(val < node.val and node.left != None):
            self._find(val, node.left)
        elif(val > node.val and node.right != None):
            self._find(val, node.right)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)

    # Iterative Method to print the height of binary tree 
    def printLevelOrder(root): 
        # Base Case 
        if root is None: 
            return
        
        # Create an empty queue for level order traversal 
        queue = [] 
    
        # Enqueue Root and initialize height 
        queue.append(root) 
    
        while(len(queue) > 0): 
            # Print front of queue and remove it from queue 
            print queue[0].data, 
            node = queue.pop(0) 
    
            #Enqueue left child 
            if node.left is not None: 
                queue.append(node.left) 
    
            # Enqueue right child 
            if node.right is not None: 
                queue.append(node.right) 

#     3
# 0     4
#   2      8
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
#tree.printTree()    
Tree().printLevelOrder(tree.root)

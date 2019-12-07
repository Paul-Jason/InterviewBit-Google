# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    
    def findPath(self,root,path,k):
        if root is None:
            return False
        path.append(root.val)
        if root.val==k:
            return True
        if (root.left!=None and self.findPath(root.left,path,k) or root.right!=None and self.findPath(root.right,path,k)):
            return True
        path.pop()
        return False
        
    def lca(self, A, B, C):
        path1 = []
        path2 = []
        if(not self.findPath(A,path1,B) or not self.findPath(A,path2,C)):
            return -1
        i=0
        while(i<len(path1) and i< len(path2)):
            if path1[i]!=path2[i]:
                break
            i=i+1 
        return path1[i-1]   

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

print(Solution().lca(root,6,4))
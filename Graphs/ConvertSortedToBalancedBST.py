# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def sortedListToBST(self, A):
        #Get the sorted array from linked list 
        #So that forming the balanced BST will take only O(n) time
        sortedArr = []
        temp = A
        while(temp):
            sortedArr.append(temp.val)
            temp = temp.next
        root = self.sortedArrToBalancedBST(sortedArr)
        return root
    
    def sortedArrToBalancedBST(self, arr):
        if not arr:
            return None
        #find middle
        mid = (len(arr))//2
        #Make middle the root element 
        root = TreeNode(arr[mid])
        #repeat the same for left part
        root.left = self.sortedArrToBalancedBST(arr[:mid])
        #right
        root.right = self.sortedArrToBalancedBST(arr[mid+1:])
        return root
        
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
Solution().sortedListToBST(head)

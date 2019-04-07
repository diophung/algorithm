"""
Problem: Given a binary tree, return the vertical order traversal
of its nodes' values. (ie, from top to bottom, column by column).
If two nodes are in the same row and column, the order should be
from left to right.
Examples:

Given binary tree [3,9,20,null,null,15,7],
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]

Given binary tree [3,9,8,4,0,1,7],
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]

Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5]
(0's right child is 2 and 1's left child is 5),
     3
    /  \
   9    8
  /\    /\
 4  0   1 7
     \  /
      2 5
return its vertical order traversal as:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]

Algorithm:
use hashtable, key is the vertical column, value is the node valls
as we traverse the tree, we check if the column is inside the table
if not, we

"""

# Definition for a binary tree node.
import Queue


class TreeNode:
    
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTreeMultiOrder:
    @staticmethod
    def pre_order(root):
        path = []
        if root is not None:
            path.append(root.val)
        if root is not None and root.left is not None:
            path += BinaryTreeMultiOrder.pre_order(root.left)
        if root is not None and root.right is not None:
            path += BinaryTreeMultiOrder.pre_order(root.right)
        
        return path
    
    @staticmethod
    def horizontal_order(root):
        if root is None:
            return None
        q = Queue.Queue()
        q.put(root)
        while q.empty() is False:
            current_node = q.get(False)
            print(current_node.val)
            if current_node.left is not None:
                q.put(current_node.left)
            if current_node.right is not None:
                q.put(current_node.right)
        return q
    
    @staticmethod
    def vertical_order(root):
        output = []
        maps = {}
        left_most, right_most = 0, 0
        nodes = Queue.Queue()
        nodes.put(root)
        cols = Queue.Queue()
        107
        
        cols.put(0)
        while nodes.empty() is False:
            node = nodes.get(False)
            col = cols.get(False)
            
            if col not in maps:
                maps[col] = []
            maps[col].append(node.val)
            
            if node.left is not None:
                nodes.put(node.left)
                cols.put(col - 1)
                left_most = min(left_most, col - 1)
            if node.right is not None:
                nodes.put(node.right)
                cols.put(col + 1)
                right_most = max(right_most, col + 1)
        
        for i in range(left_most, right_most + 1):
            output.append(maps[i])
        return output
    
    @staticmethod
    def array_to_tree(index, arr):
        root = None
        if index > len(arr):
            return None
        if arr[index - 1] is not None:
            root = TreeNode(arr[index - 1])
            root.left = BinaryTreeMultiOrder.array_to_tree(2 * index, arr)
            root.right = BinaryTreeMultiOrder.array_to_tree(2 * index + 1, arr)
        return root
    
    @staticmethod
    def build_tree_from_array(self, arr):
        return BinaryTreeMultiOrder.arrayToTree(1, arr)
    
    @staticmethod
    def print_vertical_order(arr):
        root = BinaryTreeMultiOrder.array_to_tree(1, arr)
        result = BinaryTreeMultiOrder.vertical_order(root)
        print(result)
    
    @staticmethod
    def print_horizontal_order(arr):
        root = BinaryTreeMultiOrder.array_to_tree(1, arr)
        result = BinaryTreeMultiOrder.horizontal_order(root)
        while not result.empty():
            print(result.get(False))
    
    @staticmethod
    def pretty_print(root):
        """
        print a completed balanced binary tree in a readable manner
        i.e: each node is distributed evenly on the line
        soln:
        given k: the height of current level (from leave level)
        left child: padd left 2^k - 1
        right child: padd right 2^k - 1

        Level   3   *******1*******
        Level   2   ***2*******3***
        Level   1   *4***5***6***7*
        Level   0   1*2*3*4*5*6*7*8

        or
                       1        
                   2       3    
                 4   5   6   7  
                1 2 3 4 5 6 7 8

        """
        if root:
            print(root.val)
        if root.left:
            BinaryTreeMultiOrder.pretty_print(root.left)
        if root.right:
            BinaryTreeMultiOrder.pretty_print(root.right)


arr = [3, 9, 8, 4, 0, 1, 7]
BinaryTreeMultiOrder.print_vertical_order(arr)
print()
BinaryTreeMultiOrder.print_horizontal_order(arr)
print()

arr = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 8]
BinaryTreeMultiOrder.print_vertical_order(arr)
print()
BinaryTreeMultiOrder.print_horizontal_order(arr)
print()

"""
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7



expect:
[
 [3]
 [9, 8]
 [4, 0, 1, 7]
]
 """

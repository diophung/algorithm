# Tree traversal : post, in, pre-order traversal
from datastructure.TreeNode import BinaryTreeNode


class TreeTraversal:
    def post_order(self, root: BinaryTreeNode):
        if root and root.left:
            self.post_order(root.left)
        if root and root.right:
            self.post_order(root.right)
        if root.value:
            print(root.value)

    def in_order(self, root):
        if root and root.left:
            self.post_order(root.left)
        if root.val:
            print(root.val)
        if root and root.right:
            self.post_order(root.right)

    def pre_order(self, root):
        if root.val:
            print(root.val)
        if root and root.left:
            self.post_order(root.left)
        if root and root.right:
            self.post_order(root.right)

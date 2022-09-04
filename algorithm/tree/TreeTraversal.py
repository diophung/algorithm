# Tree traversal : post, in, pre-order traversal


class TreeTraversal:
    def post_order(self, root):
        if root and root.left:
            self.post_order(root.left)
        if root and root.right:
            self.post_order(root.right)
        if root:
            print(root)


# Post-order

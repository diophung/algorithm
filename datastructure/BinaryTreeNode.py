import TreeNode


class BinaryTreeNode(TreeNode):
    def __init__(self, value, left, right, node_id):
        super().__init__(node_id, value)
        self._val = value
        self._left = left
        self._right = right

    @property
    def left(self):
        return self.left

    @property
    def right(self):
        return self._right

    @property
    def val(self):
        return self._val


class BinTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Function to insert nodes in level order
def insert_level_order(array, i, n):
    _root = None
    if i < n:
        _root = BinTreeNode(array[i])
        _root.left = insert_level_order(array, 2 * i + 1, n)
        _root.right = insert_level_order(array, 2 * i + 2, n)
    return _root


# Function to print tree nodes in
# InOrder fashion
def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        print(root.data, end=" ")
        in_order_traversal(root.right)


# Driver Code
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
    n = len(arr)
    root = insert_level_order(arr, 0, n)
    in_order_traversal(root)

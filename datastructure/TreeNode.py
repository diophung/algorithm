class TreeNode(object):
    def __init__(self, node_id, value=None, children=None):
        self._id = node_id
        self._value = value if value else node_id
        self._children = children if children else []

    @property
    def children(self):
        if self._children:
            return self._children
        return []

    @property
    def value(self):
        return self._value;

    @property
    def id(self):
        return self._id

    def add_child(self, child):
        self._children.append(child)

    def get_child(self, child_id):
        for c in self.children:
            if c.id == child_id:
                return c
        return None

    def is_ancestor(self, node):
        """
        Check if this is an ancestor of node.
        """
        if not node or not self.value:
            return False
        if self.value == node.value:
            return True
        else:
            for child in self.children:
                if child.is_ancestor(node):
                    return True
        return False


class BinaryTreeNode(TreeNode):
    left = None
    right = None

    def __init__(self, value: int, left, right):
        self.value = value
        self.left = left
        self.right = right

    @property
    def left(self):
        return self.left

    @property
    def right(self):
        return self.right


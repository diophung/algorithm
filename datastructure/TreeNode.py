class TreeNode(object):
    def __init__(self, node_id, value=None, children=None):
        self._id = node_id
        self._value = value if value else node_id
        self._children = children if children else []

    @property
    def value(self):
        return self._value;

    @property
    def id(self):
        return self._id

    def add_child(self, child):
        self._children.append(child)

    def get_children(self):
        return self._children

    def get_single_child(self, child_id):
        for c in self.get_children():
            if c.id == child_id:
                return c
        return None

    def is_ancestor(self, node):
        """
        Check if this is an ancestor of node.
        """
        if not node or not self.value:
            return False
        if self.value == node.val:
            return True
        else:
            for child in self.get_children():
                if child.is_ancestor(node):
                    return True
        return False




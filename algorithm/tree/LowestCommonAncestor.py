
class LowestCommonAncestor():
    """
    Find the lowest common ancestor in a tree for any 2 nodes
    """

    def __init__(self):
        pass

    def lowest_common_ancestor(self, root, me, other):
        """
        Get lowest common ancestor
        :param root: TreeNode
        :param me: TreeNode
        :param other: TreeNode
        :return: the lowest common ancestor of me and other
        """
        if not root:
            return None
        
        # if root a common ancestor
        if root.is_ancestor(me) and root.is_ancestor(other):
            for child in root.children:
                if child.is_ancestor(me) and child.is_ancestor(other):
                    return self.lowest_common_ancestor(child, me, other)
            return root
        else:
            return None



import datastructure.TreeNode


class LowestCommonAncestor:
    """
    Find the lowest common ancestor in a tree for any 2 nodes
    """

    def lowest_common_ancestor(self, root, me, other):
        """
        Get the lowest common ancestor
        :param root: TreeNode
        :param me: TreeNode
        :param other: TreeNode
        :return: the lowest common ancestor of me and other
        """
        if not root:
            return None

        # start at the root
        if root.is_ancestor(me) and root.is_ancestor(other):
            # keep going down to another level
            # until the new root is no longer a common ancestor
            for child in root.get_children():
                if child.is_ancestor(me) and child.is_ancestor(other):
                    return self.lowest_common_ancestor(child, me, other)
            return root
        else:
            return None

import unittest
import datastructure.TreeNode


def node_by_level(curr_node, curr_lvl, target_lvl):
    """Print all nodes of a tree at a level"""
    res = []
    if curr_lvl == target_lvl:
        res += [curr_node]
    else:
        for c in curr_node.get_children():
            res += node_by_level(c, curr_lvl + 1, target_lvl)
    return res


class TreeOpsTest(unittest.TestCase):
    
    def test_print_by_level(self):
        root = datastructure.TreeNode.TreeNode(0)
        root.add_child(datastructure.TreeNode.TreeNode(1))
        root.add_child(datastructure.TreeNode.TreeNode(2))
        
        root.get_single_child(1).add_child(datastructure.TreeNode.TreeNode(3))
        root.get_single_child(2).add_child(datastructure.TreeNode.TreeNode(4))
        
        expected = [3, 4]
        nodes = [i.id for i in node_by_level(root, 1, 3)]
        self.assertEquals(expected, nodes)

        expected = [1, 2]
        nodes = [i.id for i in node_by_level(root, 1, 2)]
        self.assertEquals(expected, nodes)

        expected = [0]
        nodes = [i.id for i in node_by_level(root, 1, 1)]
        self.assertEquals(expected, nodes)

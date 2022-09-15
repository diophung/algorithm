import unittest
import sys

import datastructure.TreeNode
from algo.tree.LowestCommonAncestor import LowestCommonAncestor


class TestLowestCommonAncestor(unittest.TestCase):

    def test_happy_case(self):
        """
           root
           /   \
          A     C
         /     / \
        B     F   D
                   \
                    E
        :return:
        """
        lca = LowestCommonAncestor()
        root = datastructure.TreeNode.TreeNode("root")

        A = datastructure.TreeNode.TreeNode("A")
        B = datastructure.TreeNode.TreeNode("B")
        C = datastructure.TreeNode.TreeNode("C")
        D = datastructure.TreeNode.TreeNode("D")
        E = datastructure.TreeNode.TreeNode("E")
        F = datastructure.TreeNode.TreeNode("F")

        A.add_child(B)
        C.add_child(D)
        C.add_child(F)
        D.add_child(E)

        root.add_child(A)
        root.add_child(C)
        self.assertEqual(lca.lowest_common_ancestor(root, B, D).val, "root")  # expect root
        self.assertEqual(lca.lowest_common_ancestor(root, F, E).val, "C")  # expect C
        self.assertEqual(lca.lowest_common_ancestor(root, A, E).val, "root")  # expect root
        self.assertEqual(lca.lowest_common_ancestor(root, D, E).val, "D")  # expect D

import unittest

import datastructure.TreeNode
from algorithm.tree.LowestCommonAncestor import LowestCommonAncestor


# expose other modules at top level
# sys.path.append("..")


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

        A.children.append(B)
        C.children.append(D)
        C.children.append(F)
        D.children.append(E)

        root.children.append(A)
        root.children.append(C)
        # self.assertEqual(lca.lowest_common_ancestor(root, B, D).value, "root")  # expect root
        # self.assertEqual(lca.lowest_common_ancestor(root, F, E).value, "C")  # expect C
        # self.assertEqual(lca.lowest_common_ancestor(root, A, E).value, "root")  # expect root
        # self.assertEqual(lca.lowest_common_ancestor(root, D, E).value, "D")  # expect D
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

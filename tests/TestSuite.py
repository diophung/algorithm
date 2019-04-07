import sys
import unittest
import datastructure.TreeNode

# expose other modules at top level
sys.path.append("..")


class TestConverter(unittest.TestCase):
    def excel_column_converter(self):
        converter = ()
        self.assertEqual(converter.convert_to_title(1), "A")
        self.assertEqual(converter.convert_to_title(703), "AAA")
        self.assertEqual(converter.convert_to_index("A"), 1)
        self.assertEqual(converter.convert_to_index("AAA"), 703)

    def lowest_common_manager(self):
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
        lca = LCA()
        root = datastructure.TreeNode.TreeNode("root")
        l1 = datastructure.TreeNode.TreeNode("l1")
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
        self.assertEqual(lca.lowest_common_ancestor(root, B, D).value, "root")  # expect root
        self.assertEqual(lca.lowest_common_ancestor(root, F, E).value, "C")  # expect C
        self.assertEqual(lca.lowest_common_ancestor(root, A, E).value, "root")  # expect root
        self.assertEqual(lca.lowest_common_ancestor(root, D, E).value, "D")  # expect D
        self.assertEquals(lca.lowest_common_ancestor(root, root, l1), None)


if __name__ == '__main__':
    unittest.main()

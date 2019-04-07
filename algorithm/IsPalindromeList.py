# Problem: given singly linked list, determine if this is Palindrome list
# For e.g.:  1->2->3->2->1 is a palindrom list while 1->2->3->2->2 is not.


class IsPalindromeList:
    @staticmethod
    def is_palindrome_list(head_node):
        """
        return True if this is a palindrome list
        """
        strVal = ""
        while head_node is not None:
            strVal += str(head_node.nodeValue)
            head_node = head_node.nextNode
        return IsPalindromeList.is_palindrome(strVal)

    @staticmethod
    def is_palindrome(string):
        reverse = ''.join(reversed(string))
        return reverse == string


class Node:
    nodeValue = None
    nextNode = None

    def __init__(self, nodeValue, nextNode):
        self.nodeValue = nodeValue
        self.nextNode = nextNode


n5 = Node(1, None)
n4 = Node(2, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
prob = IsPalindromeList()
print(str(prob.is_palindrome_list(n1)))  # expect True


n5 = Node(1, None)
n4 = Node(99, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
print(str(prob.is_palindrome_list(n1)))  # expect False

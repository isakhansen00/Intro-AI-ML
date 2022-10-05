from binarytree import Node
from collections import namedtuple

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
        self.size = 0
        """ Initialize binary search tree

        # Inputs:
        root:    (optional) An instance of Node which is the root of the tree

        # Notes:
        If a root is supplied, validate that the tree meets the requirements
        of a search tree. If not, raise ValueError.
        """

    def get_root(self):
        return self.root

    def insert(self, node_value):
        if self.root == None:
            self.root = Node(node_value)  # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            while current != None:
                if node_value < current.value:
                    parent = current
                    current = current.left
                elif node_value > current.value:
                    parent = current
                    current = current.right
                else:
                    return False  # Duplicate node not inserted

            # Create the new node and attach it to the parent node
            if node_value < parent.value:
                parent.left = Node(node_value)
            else:
                parent.right = Node(node_value)

        self.size += 1  # Increase tree size
        return True  # Element inserted
        """Insert a new node into the tree

        # Inputs:
        value:    Value of new node

        # Notes:
        The method should issue a warning if the value already exists in the tree.
        See https://docs.python.org/3/library/warnings.html#warnings.warn
        In the case of duplicate values, leave the tree unchanged.
        """

    def find(self, node_value):
        current = self.root  # Start from the root

        while current != None:
            if node_value < current.value:
                current = current.left
            elif node_value > current.value:
                current = current.right
            else:  # element matches current.element
                return print(
                    f"The value given; {current.value} exists in the tree"
                )  # Element is found

        raise KeyError("Number not found, please try again")

    def _delete_helper(self, root, nodes):
        # Base Case
        if root is None:
            return root

        if nodes is None:
            raise KeyError("Value not found")

        # Recursive calls for ancestors of
        # node to be deleted
        if nodes < root.value:
            root.left = self._delete_helper(root.left, nodes)
            return root

        elif nodes > root.value:
            root.right = self._delete_helper(root.right, nodes)
            return root

        # We reach here when root is the node
        # to be deleted.

        # If root node is a leaf node

        if root.left is None and root.right is None:
            return None

        # If one of the children is empty

        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # If both children exist

        succesor_parent = root

        # Find the inorder successor
        succesor = root.right

        while succesor.left != None:
            succesor_parent = succesor
            succesor = succesor.left

        # Delete successor
        if succesor_parent != root:
            succesor_parent.left = succesor.right
        else:
            succesor_parent.right = succesor.right

        # Copy Successor Data to root

        root.value = succesor.value

        return root

    def delete(self, node_value):
        return self._delete_helper(self.root, node_value)

        """Delete node with given value

        # Inputs:
        value:    Value of node to be deleted

        # Notes:
        This function should handle a number of "regular" cases:
        - Deleting a leaf node
        - Deleting a node with one child
        - Deleting a node with two childen
          (the node should be replaced with its inorder successor)

        It should also handle the following "edge cases":
        - Value not found in tree (raise KeyError)
        - Deleting the root node
        - Calling delete on an empty tree (raise KeyError)
        """

    def level(self, node_value):
        current = self.root  # Start from the root
        level = 0

        while current != None:
            if node_value < current.value:
                current = current.left
                level += 1
            elif node_value > current.value:
                current = current.right
                level += 1
            else:  # element matches current.element
                return print(
                    f"The level of the node: {node_value} is {level}"
                )  # Element is found

        raise KeyError("Number not found, please try again")


test_tree = BinarySearchTree()
test_tree = BinarySearchTree()
test_tree.insert(7)
test_tree.insert(4)
test_tree.insert(2)
test_tree.insert(6)
test_tree.insert(1)
test_tree.insert(5)
test_tree.insert(13)
test_tree.insert(15)
test_tree.insert(9)
test_tree.insert(8)
test_tree.insert(11)
test_tree.insert(12)
print(test_tree.get_root())
test_tree.delete(1)
test_tree.delete(11)
test_tree.delete(4)
test_tree.delete(7)
print(test_tree.get_root())


new_test_tree = BinarySearchTree()
with open("random_numbers.txt") as number_file:
    numbers = [line.strip() for line in number_file]

for i in numbers:
    new_test_tree.insert(int(i))

new_test_tree.level(584330)
new_test_tree.level(217258)
new_test_tree.level(375195)
new_test_tree.level(136006)
new_test_tree.level(560440)
new_test_tree.level(12239)

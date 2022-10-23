from binarytree import Node
import warnings

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

        if self.root != None and self.root.is_bst:
            pass
        elif self.root == None:
            pass
        else:
            raise ValueError("Does not satisfy the requirements of a Binary Search Tree")


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
                    warnings.warn(f"Duplicate value can not be added to the tree")
                    return False # Duplicate node not inserted
                    

            # Create the new node and attach it to the parent node
            if node_value < parent.value:
                parent.left = Node(node_value)
            else:
                parent.right = Node(node_value)

        self.size += 1 
        return True # node has succesfully been inserted


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

        if root is None:
            return root

        if nodes is None:
            raise KeyError("Value not found")

        # Recursively iterate through tree to find node to be deleted
        if nodes < root.value:
            root.left = self._delete_helper(root.left, nodes)
            return root

        # Same as above
        elif nodes > root.value:
            root.right = self._delete_helper(root.right, nodes)
            return root

        # Case to handle if the root node is the only node
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

        succesor_parent = root

        # Finding the inorder successor 
        succesor = root.right

        while succesor.left != None:
            succesor_parent = succesor
            succesor = succesor.left

        # Deleting the successor
        if succesor_parent != root:
            succesor_parent.left = succesor.right
        else:
            succesor_parent.right = succesor.right


        root.value = succesor.value

        return root

    def delete(self, node_value):       
        if self.root == None:
            raise KeyError("Tree is already empty")
        elif node_value < self.root.min_node_value or node_value > self.root.max_node_value:
            raise KeyError("Given number is not in the tree, please try another number")

        return self._delete_helper(self.root, node_value)



    def level(self, node_value):
        current = self.root 
        level = 1

        while current != None:
            if node_value < current.value:
                current = current.left
                level += 1
            elif node_value > current.value:
                current = current.right
                level += 1
            else:  # element matches current.element
                return print(
                    f"The level of the node {node_value}: is {level}"
                ) 

        raise KeyError("Number not found, please try again")


# OPPGAVE 2
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
#test_tree.insert(12)
print(test_tree.get_root())
test_tree.delete(1)
test_tree.delete(11)
test_tree.delete(4)
test_tree.delete(7)
print(test_tree.get_root())
#test_tree2 = BinarySearchTree()
#test_tree2.delete(2)



# OPPGAVE 3
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

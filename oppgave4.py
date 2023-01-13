class MyNode:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

def met(node):
    ret_str = ''
    if node.left != None:
        ret_str += met(node.left)
    ret_str += str(node.value) + ', '
    if node.right != None:
        ret_str += met(node.right)
    return ret_str


def main():
    test = MyNode(15)
    test.left = MyNode(8)
    test.left.right = MyNode(12)
    test.right = MyNode(21)
    test.right.left = MyNode(18)
    test.right.right = MyNode(32)

    print(met(test))

main()
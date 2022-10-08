from BinaryTree import BinaryTree
from BinaryTreeNode import BinaryTreeNode
from collections import namedtuple
import pytest

Persons = namedtuple("Person", ["etternavn", "fornavn", "addresse", "zip", "city"])

person_one = Persons(
    "Kristiansen", "Morten Kristian", "Leinahytta 36", "7224", "Melhus"
)
person_two = Persons("Oldervik", "Shari Lill", "Kroka 84", "5948", "Fedje")
person_three = Persons("Gjerstad", "Torkjell", "Hosteland 283", "1361", "Østerås")
person_four = Persons("Nymann", "Roy-Øystein", "Honeset 77", "7033", "Trondheim")
person_five = Persons("Østby", "Frank", "Worseth 57", "7414", "Trondheim")
person_six = Persons(
    "Vestly Skivik", "Jahn Fredrik", "Linngård 22", "1451", "Nesoddtangen"
)
person_seven = Persons("Hinnerud", "Johnny", "Lørum Mellem 50", "6507", "Kristiansund")

test_tree = BinaryTree()
node_one = BinaryTreeNode(person_one)
node_two = BinaryTreeNode(person_two)
node_three = BinaryTreeNode(person_three)
node_four = BinaryTreeNode(person_four)
node_five = BinaryTreeNode(person_five)
node_six = BinaryTreeNode(person_six)
node_seven = BinaryTreeNode(person_seven)
node_one = test_tree.insert(value=node_one)
node_two = test_tree.insert(value=node_two)
node_three = test_tree.insert(value=node_three)
node_four = test_tree.insert(value=node_four)
node_five = test_tree.insert(value=node_five)


def test_make_tree_without_BTN():
    test_tree = BinaryTree(person_one)
    assert isinstance(test_tree, BinaryTree)

def test_insert_root():
    test_tree = BinaryTree()
    node_one = BinaryTreeNode(person_one)
    node_two = BinaryTreeNode(person_one)
    test_tree.insert(value = node_one)
    test_tree.insert(value = node_two)


def test_make_tree_with_BTN():
    root_node = BinaryTreeNode(person_one)
    test_tree = BinaryTree(root_node)
    assert isinstance(test_tree, BinaryTree)


def test_find_left_most():

    left_most = test_tree.findLeftMost(node_one)
    assert left_most.value.value == Persons(
        etternavn="Gjerstad",
        fornavn="Torkjell",
        addresse="Hosteland 283",
        zip="1361",
        city="Østerås",
    )


def test_findmin():

    left_most = test_tree.findMin()
    assert left_most.value.value == Persons(
        etternavn="Gjerstad",
        fornavn="Torkjell",
        addresse="Hosteland 283",
        zip="1361",
        city="Østerås",
    )


def test_find_right_most():

    left_most = test_tree.findRightMost(node_one)
    assert left_most.value.value == Persons(
        etternavn="Østby",
        fornavn="Frank",
        addresse="Worseth 57",
        zip="7414",
        city="Trondheim",
    )


def test_find_max():

    left_most = test_tree.findMax()
    assert left_most.value.value == Persons(
        etternavn="Østby",
        fornavn="Frank",
        addresse="Worseth 57",
        zip="7414",
        city="Trondheim",
    )

def test_find_max_using_find():
    test_tree = BinaryTree()
    node_one = BinaryTreeNode(person_one)
    node_two = BinaryTreeNode(person_two)
    node_three = BinaryTreeNode(person_three)
    node_four = BinaryTreeNode(person_four)
    node_five = BinaryTreeNode(person_five)
    test_tree.insert(value=node_one)
    test_tree.insert(value=node_two)
    test_tree.insert(value=node_three)
    test_tree.insert(value=node_four)
    test_tree.insert(value=node_five)
    found = test_tree.find(node_five)
    assert found.value.value == Persons(
        etternavn="Østby",
        fornavn="Frank",
        addresse="Worseth 57",
        zip="7414",
        city="Trondheim",
    )

def find_min_using_find():
    test_tree = BinaryTree()
    node_one = BinaryTreeNode(person_one)
    node_two = BinaryTreeNode(person_two)
    node_three = BinaryTreeNode(person_three)
    node_four = BinaryTreeNode(person_four)
    node_five = BinaryTreeNode(person_five)
    test_tree.insert(value=node_one)
    test_tree.insert(value=node_two)
    test_tree.insert(value=node_three)
    test_tree.insert(value=node_four)
    test_tree.insert(value=node_five)
    found = test_tree.find(node_three)
    assert found.value.value == Persons(
        etternavn="Gjerstad",
        fornavn="Torkjell",
        addresse="Hosteland 283",
        zip="1361",
        city="Østerås",
    )

def test_deleteMin_with_only_root_and_right_value():
    test_tree = BinaryTree()
    node_one = BinaryTreeNode(person_one)
    node_two = BinaryTreeNode(person_four)
    node_one = test_tree.insert(value=node_one)
    node_two = test_tree.insert(value=node_two)
    test_tree.deleteMin()
    min_value = test_tree.findMin()
    assert min_value.value.value == Persons(
        etternavn="Nymann",
        fornavn="Roy-Øystein",
        addresse="Honeset 77",
        zip="7033",
        city="Trondheim",
    )


person_four = Persons("Nymann", "Roy-Øystein", "Honeset 77", "7033", "Trondheim")


def test_delete_min():
    test_tree.deleteMin()
    left_most = test_tree.findLeftMost(node_one)
    assert left_most.value.value == Persons(
        etternavn="Kristiansen",
        fornavn="Morten Kristian",
        addresse="Leinahytta 36",
        zip="7224",
        city="Melhus",
    )


def test_delete_min_with_right_value():
    test_tree = BinaryTree()
    node_one = BinaryTreeNode(person_one)
    node_two = BinaryTreeNode(person_two)
    node_three = BinaryTreeNode(person_three)
    node_four = BinaryTreeNode(person_four)
    node_five = BinaryTreeNode(person_five)
    node_six = BinaryTreeNode(person_six)
    node_seven = BinaryTreeNode(person_seven)
    node_one = test_tree.insert(value=node_one)
    node_two = test_tree.insert(value=node_two)
    node_three = test_tree.insert(value=node_three)
    node_four = test_tree.insert(value=node_four)
    node_five = test_tree.insert(value=node_five)
    node_six = test_tree.insert(value=node_six)
    node_seven = test_tree.insert(value=node_seven)
    test_tree.deleteMin()
    left_most = test_tree.findLeftMost(node_one)
    assert left_most.value.value == Persons(
        etternavn="Hinnerud",
        fornavn="Johnny",
        addresse="Lørum Mellem 50",
        zip="6507",
        city="Kristiansund",
    )


def test_delete_max():
    test_tree = BinaryTree()
    node_one = BinaryTreeNode(person_one)
    node_two = BinaryTreeNode(person_two)
    node_three = BinaryTreeNode(person_three)
    node_four = BinaryTreeNode(person_four)
    node_five = BinaryTreeNode(person_five)
    node_seven = BinaryTreeNode(person_seven)
    node_one = test_tree.insert(value=node_one)
    node_two = test_tree.insert(value=node_two)
    node_three = test_tree.insert(value=node_three)
    node_four = test_tree.insert(value=node_four)
    node_five = test_tree.insert(value=node_five)
    node_seven = test_tree.insert(value=node_seven)
    test_tree.deleteMax()
    left_most = test_tree.findRightMost(node_one)
    assert left_most.value.value == Persons(
        etternavn="Oldervik",
        fornavn="Shari Lill",
        addresse="Kroka 84",
        zip="5948",
        city="Fedje",
    )


def test_delete_max_with_left_value():
    test_tree = BinaryTree()
    node_one = BinaryTreeNode(person_one)
    node_two = BinaryTreeNode(person_two)
    node_three = BinaryTreeNode(person_three)
    node_four = BinaryTreeNode(person_four)
    node_five = BinaryTreeNode(person_five)
    node_six = BinaryTreeNode(person_six)
    node_seven = BinaryTreeNode(person_seven)
    node_one = test_tree.insert(value=node_one)
    node_two = test_tree.insert(value=node_two)
    node_three = test_tree.insert(value=node_three)
    node_four = test_tree.insert(value=node_four)
    node_five = test_tree.insert(value=node_five)
    node_six = test_tree.insert(value=node_six)
    node_seven = test_tree.insert(value=node_seven)
    test_tree.deleteMax()
    left_most = test_tree.findRightMost(node_one)
    assert left_most.value.value == Persons(
        etternavn="Vestly Skivik",
        fornavn="Jahn Fredrik",
        addresse="Linngård 22",
        zip="1451",
        city="Nesoddtangen",
    )


def test_delete():
    test_tree = BinaryTree()
    node_one = BinaryTreeNode(person_one)
    node_two = BinaryTreeNode(person_two)
    node_three = BinaryTreeNode(person_three)
    node_four = BinaryTreeNode(person_four)
    node_five = BinaryTreeNode(person_five)
    node_six = BinaryTreeNode(person_six)
    node_seven = BinaryTreeNode(person_seven)
    test_tree.insert(value=node_one)
    test_tree.insert(value=node_two)
    test_tree.insert(value=node_three)
    test_tree.insert(value=node_four)
    test_tree.insert(value=node_five)
    test_tree.insert(value=node_six)
    test_tree.insert(value=node_seven)
    test_tree.delete(node_two)
    right_most = test_tree.findMax()
    assert right_most.value.value == Persons(
        etternavn="Østby",
        fornavn="Frank",
        addresse="Worseth 57",
        zip="7414",
        city="Trondheim",
    )

def test_delete_left_most():
    test_tree = BinaryTree()
    node_one = BinaryTreeNode(person_one)
    node_two = BinaryTreeNode(person_two)
    node_three = BinaryTreeNode(person_three)
    node_four = BinaryTreeNode(person_four)
    node_five = BinaryTreeNode(person_five)
    node_six = BinaryTreeNode(person_six)
    node_seven = BinaryTreeNode(person_seven)
    test_tree.insert(value=node_one)
    test_tree.insert(value=node_two)
    test_tree.insert(value=node_three)
    test_tree.insert(value=node_four)
    test_tree.insert(value=node_five)
    test_tree.insert(value=node_six)
    test_tree.insert(value=node_seven)
    test_tree.delete(node_three)
    left_most = test_tree.findMin()
    assert left_most.value.value == Persons(
        etternavn="Hinnerud",
        fornavn="Johnny",
        addresse="Lørum Mellem 50",
        zip="6507",
        city="Kristiansund",
    )

def test_delete_left_child_of_right_most():
    test_tree = BinaryTree()
    node_one = BinaryTreeNode(person_one)
    node_two = BinaryTreeNode(person_two)
    node_three = BinaryTreeNode(person_three)
    node_four = BinaryTreeNode(person_four)
    node_five = BinaryTreeNode(person_five)
    node_six = BinaryTreeNode(person_six)
    node_seven = BinaryTreeNode(person_seven)
    test_tree.insert(value=node_one)
    test_tree.insert(value=node_two)
    test_tree.insert(value=node_three)
    test_tree.insert(value=node_four)
    test_tree.insert(value=node_five)
    test_tree.insert(value=node_six)
    test_tree.insert(value=node_seven)
    test_tree.delete(node_six)
    right_most = test_tree.findMax()
    assert right_most.left == None

def test_delete_max_with_left():
    test_tree = BinaryTree()
    node_one = BinaryTreeNode(person_one)
    node_two = BinaryTreeNode(person_two)
    node_three = BinaryTreeNode(person_three)
    node_four = BinaryTreeNode(person_four)
    node_five = BinaryTreeNode(person_five)
    node_six = BinaryTreeNode(person_six)
    node_seven = BinaryTreeNode(person_seven)
    test_tree.insert(value=node_one)
    test_tree.insert(value=node_two)
    test_tree.insert(value=node_three)
    test_tree.insert(value=node_four)
    test_tree.insert(value=node_five)
    test_tree.insert(value=node_six)
    test_tree.insert(value=node_seven)
    test_tree.delete(node_five)
    right_most = test_tree.findMax()
    assert right_most.left == None

def test_delete_non_existent_node():
    test_tree = BinaryTree()
    node_one = BinaryTreeNode(person_one)
    test_tree.insert(value=node_one)  
    assert test_tree.delete(None) == None

def test_delete_root():
    test_tree = BinaryTree()
    node_one = BinaryTreeNode(person_one)
    test_tree.insert(value=node_one)  
    test_tree.delete(node_one)
    assert test_tree._root == None
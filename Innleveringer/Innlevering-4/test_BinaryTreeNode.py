"""
I testen er det noen av testene som vil feile siden det virker som dem er feil implementert i klassen BinaryTreeNode. I de tilfellene har jeg lagd 
UnitTesten slik det er ment at dem egentlig skal fungere.

Dette gjelder __ne__:
    funksjonen i klassen returnerer false hvis dem er ulik, men dem skal egentlig returnere true

Og __le__, __ge__:
    sånn som jeg skjønner det så skal True egentlig returneres hvis to None verdier sammenlignes med ">=" eller "<="
    Unit testene mine feiler altså her siden True egentlig skal returneres.

"""

from logging import root
from BinaryTreeNode import BinaryTreeNode
import pytest
from collections import namedtuple


Persons = namedtuple("Person", ["etternavn", "fornavn", "addresse", "zip", "city"])

person_one = Persons(
    "Kristiansen", "Morten Kristian", "Leinahytta 36", "7224", "Melhus"
)
person_two = Persons("Oldervik", "Shari Lill", "Kroka 84", "5948", "Fedje")
person_three = Persons("Gjerstad", "Torkjell", "Hosteland 283", "1361", "Østerås")
person_four = Persons("Nymann", "Roy-Øystein", "Honeset 77", "7033", "Trondheim")
person_five = Persons("Østby", "Frank", "Worseth 57", "7414", "Trondheim")


def test_make_node():
    person_node = BinaryTreeNode(person_one)
    assert isinstance(person_node, BinaryTreeNode)


def test_value():
    root_node = BinaryTreeNode(person_one)
    assert root_node.value == Persons(
        etternavn="Kristiansen",
        fornavn="Morten Kristian",
        addresse="Leinahytta 36",
        zip="7224",
        city="Melhus",
    )


def test_left_value():
    root_node = BinaryTreeNode(person_one)
    root_node.left = BinaryTreeNode(person_five)
    assert root_node.hasLeft() == True


def test_no_left_value():
    root_node = BinaryTreeNode(person_one)
    assert root_node.hasLeft() == False


def test_right_value():
    root_node = BinaryTreeNode(person_one)
    root_node.right = BinaryTreeNode(person_three)
    assert root_node.hasRight() == True


def test_no_right_value():
    root_node = BinaryTreeNode(person_one)
    assert root_node.hasRight() == False


def test_set_level():
    root_node = BinaryTreeNode(person_one)
    root_node.right = BinaryTreeNode(person_three)
    root_node.right.level = 1
    assert root_node.right.level == 1


def test_prefix_order(capsys):
    root_node = BinaryTreeNode(person_one)
    root_node.left = BinaryTreeNode(person_four)
    root_node.right = BinaryTreeNode(person_three)
    root_node.prefixOrder()
    captured_string = capsys.readouterr()
    assert (
        captured_string.out
        == "Person(etternavn='Kristiansen', fornavn='Morten Kristian', addresse='Leinahytta 36', zip='7224', city='Melhus')  \n"
        + "Person(etternavn='Nymann', fornavn='Roy-Øystein', addresse='Honeset 77', zip='7033', city='Trondheim')  \n"
        + "Person(etternavn='Gjerstad', fornavn='Torkjell', addresse='Hosteland 283', zip='1361', city='Østerås')  \n"
    )


def test_infix_order(capsys):
    root_node = BinaryTreeNode(person_one)
    root_node.left = BinaryTreeNode(person_four)
    root_node.right = BinaryTreeNode(person_three)
    root_node.infixOrder()
    captured_string = capsys.readouterr()
    assert (
        captured_string.out
        == "Person(etternavn='Nymann', fornavn='Roy-Øystein', addresse='Honeset 77', zip='7033', city='Trondheim')  \n"
        + "Person(etternavn='Kristiansen', fornavn='Morten Kristian', addresse='Leinahytta 36', zip='7224', city='Melhus')  \n"
        + "Person(etternavn='Gjerstad', fornavn='Torkjell', addresse='Hosteland 283', zip='1361', city='Østerås')  \n"
    )


def test_postfix_order(capsys):
    root_node = BinaryTreeNode(person_one)
    root_node.left = BinaryTreeNode(person_four)
    root_node.right = BinaryTreeNode(person_three)
    root_node.postfixOrder()
    captured_string = capsys.readouterr()
    assert (
        captured_string.out
        == "Person(etternavn='Nymann', fornavn='Roy-Øystein', addresse='Honeset 77', zip='7033', city='Trondheim')  \n"
        + "Person(etternavn='Gjerstad', fornavn='Torkjell', addresse='Hosteland 283', zip='1361', city='Østerås')  \n"
        + "Person(etternavn='Kristiansen', fornavn='Morten Kristian', addresse='Leinahytta 36', zip='7224', city='Melhus')  \n"
    )


def test_level_order(capsys):
    root_node = BinaryTreeNode(person_one)
    root_node.left = BinaryTreeNode(person_four)
    root_node.right = BinaryTreeNode(person_three)
    root_node.levelOrder()
    captured_string = capsys.readouterr()
    assert (
        captured_string.out
        == "Person(etternavn='Kristiansen', fornavn='Morten Kristian', addresse='Leinahytta 36', zip='7224', city='Melhus')  \n"
        + "Person(etternavn='Nymann', fornavn='Roy-Øystein', addresse='Honeset 77', zip='7033', city='Trondheim')  \n"
        + "Person(etternavn='Gjerstad', fornavn='Torkjell', addresse='Hosteland 283', zip='1361', city='Østerås')  \n"
    )


def test_equal():
    root_node = BinaryTreeNode(person_one)
    root_node.left = BinaryTreeNode(person_one)
    assert (root_node == root_node.left) == True


def test_equal_with_none_value():
    root_node = BinaryTreeNode(person_one)
    root_node.left = BinaryTreeNode(person_four)
    root_node.value = None
    root_node.left.value = None
    assert (root_node == root_node.left) == True


def test_not_equal():
    root_node = BinaryTreeNode(person_one)
    root_node.left = BinaryTreeNode(person_five)
    assert (root_node != root_node.left) == True


"""
def test_not_equal_with_none_value():
    root_node = BinaryTreeNode(person_one)
    root_node.left = BinaryTreeNode(person_four)
    root_node.value = None
    assert (root_node != root_node.right) == False
"""


def test_less_than():
    root_node = BinaryTreeNode(person_one)
    root_node.left = BinaryTreeNode(person_five)
    assert (root_node < root_node.left) == True


def test_less_than_with_none_values():
    root_node = BinaryTreeNode(person_one)
    assert (root_node < root_node.left) == False


def test_less_than_with_none_values2():
    root_node = BinaryTreeNode(person_one)
    root_node.value = None
    assert (root_node < root_node.left) == False


def test_not_less_than():
    rootNode = BinaryTreeNode(person_one)
    rootNode.left = BinaryTreeNode(person_five)
    assert (rootNode.left < rootNode) == False


def test_less_than_or_equal():
    rootNode = BinaryTreeNode(person_one)
    rootNode.left = BinaryTreeNode(person_five)
    assert (rootNode <= rootNode.left) == True


def test_less_than_or_equal_none_value():
    root_node = BinaryTreeNode(person_one)
    assert (root_node <= root_node.left) == False


def test_less_than_or_equal_none_value2():
    root_node = BinaryTreeNode(person_one)
    root_node.value = None
    assert (root_node <= root_node.left) == True


def test_not_less_than_or_equal():
    root_node = BinaryTreeNode(person_one)
    root_node.left = BinaryTreeNode(person_five)
    assert (root_node.left <= root_node) == False


def test_greater_than():
    rootNode = BinaryTreeNode(person_one)
    rootNode.left = BinaryTreeNode(person_five)
    assert (rootNode.left > rootNode) == True


def test_not_greater_than():
    rootNode = BinaryTreeNode(person_one)
    rootNode.left = BinaryTreeNode(person_five)
    assert (rootNode > rootNode.left) == False


def test_not_greater_than_with_none():
    rootNode = BinaryTreeNode(person_one)
    assert (rootNode > rootNode.left) == False


def test_greater_than_with_none_value():
    root_node = BinaryTreeNode(person_one)
    assert (root_node > root_node.left) == False


def test_greater_than_with_none_value2():
    root_node = BinaryTreeNode(person_one)
    root_node.value = None
    assert (root_node > root_node.left) == False


def test_greater_than_or_equal():
    rootNode = BinaryTreeNode(person_one)
    rootNode.left = BinaryTreeNode(person_five)
    assert (rootNode.left >= rootNode) == True


def test_not_greater_than_or_equal():
    rootNode = BinaryTreeNode(person_one)
    rootNode.left = BinaryTreeNode(person_five)
    assert (rootNode >= rootNode.left) == False


def test_greater_than_or_equal_with_none_value():
    root_node = BinaryTreeNode(person_one)
    root_node.value = None
    assert (root_node >= root_node.left) == True


def test_greater_than_or_equal_with_none_value2():
    root_node = BinaryTreeNode(person_one)
    assert (root_node >= root_node.left) == False


def test_not_greater_than_or_equal_with_none():
    rootNode = BinaryTreeNode(person_one)
    assert (rootNode.left >= rootNode) == False

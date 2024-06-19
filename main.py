from BinaryTree import BinaryTree

if __name__ == '__main__':
    print("Creating binary tree")
    tree = BinaryTree()

    print("Adding root")
    tree.add(7)

    print("Adding more values")
    tree.add(3)
    tree.add(9)
    tree.add(4)
    tree.add(13)
    tree.add(29)
    tree.add(42)
    tree.add(3)
    tree.add(5)
    tree.add(10)
    tree.add(1)
    tree.add(2)
    tree.add(1)

    print("Printing binary tree")
    print(tree)

    print("is value 15 in the tree?")
    print(15 in tree)
    print("is value 42 in the tree?")
    print(42 in tree)

    print("using tree.get_list()")
    print(tree.get_list())

    print("using print(list(tree))")
    print(list(tree))
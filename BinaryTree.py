from Node import Node


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.add_helper(self.root, value)

    def add_helper(self, current, value):
        if value < current:
            if current.get_left_child() is None:
                current.set_left_child(Node(value))
            else:
                self.add_helper(current.get_left_child(), value)
        else:
            if current.get_right_child() is None:
                current.set_right_child(Node(value))
            else:
                self.add_helper(current.get_right_child(), value)

    def __contains__(self, item):
        current = self.root

        # ==, <, and > operator works on Node because __eq__, __gt__, and __lt__ operator is defined.
        while current is not None:
            if current == item:
                return True
            elif item < current:
                current = current.get_left_child()
            else:
                current = current.get_right_child()

        return False

    def get_list(self):
        return self.get_list_helper(self.root)

    def get_list_helper(self, n):
        if not n:
            return []
        else:
            return self.get_list_helper(n.get_left_child()) + [n.get_value()] + self.get_list_helper(n.get_right_child())

    def __iter__(self):
        return iter(self.get_list())

    def __str__(self):
        return self.str_helper(self.root)[2:]

    def str_helper(self, n):
        if not n:
            return ""
        else:
            return self.str_helper(n.get_left_child()) + ", " + str(n.get_value()) + self.str_helper(n.get_right_child())

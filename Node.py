class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def set_value(self, value):
        self.value = value

    def __lt__(self, other):
        if type(other) is int:
            return self.value < other
        elif type(other) is Node:
            return self.value < other.get_value()

    def __gt__(self, other):
        if type(other) is int:
            return self.value > other
        elif type(other) is Node:
            return self.value() > other.get_value()

    def __eq__(self, other):
        if type(other) is int:
            return self.value == other
        elif type(other) is Node:
            return self.value() == other.get_value()
import CompanyNode


class CompanyTree:
    def __init__(self, root: "CompanyNode" = None):
        if root is None:
            self.__root = None
        elif type(root) is not CompanyNode:
            raise ValueError("Error: root company must be a CompanyNode")
        elif root.get_parent() is not None:
            raise ValueError("Error: root must be parentless")
        else:
            self.__root = root

    def set_root(self, root):
        pass

    def get_root(self):
        pass

    def __str__(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def insert_node(self, node):
        pass

    def remove_node(self, name):
        pass

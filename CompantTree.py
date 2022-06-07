import copy

import CompanyNode


class CompanyTree:
    def __init__(self, root):
        if self.verify_root(root):
            self.__root = root

    def set_root(self, root: "CompanyNode"):
        if root.verify_root():
            self.__root = root
            return True
        return False

    def get_root(self):
        return self.__root

    def __str__(self):
        treeDictionary = get_tree_dict(self.__root, {})
        text = ""
        for level in range(len(treeDictionary)):
            level += 1
            for nodeIndex in range(len(treeDictionary[level])):
                if nodeIndex == 0:
                    text += str(treeDictionary[level][nodeIndex])
                else:
                    text += " * " + str(treeDictionary[level][nodeIndex])
            text += "\n"
        return text

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def insert_node(self, node):
        pass

    def remove_node(self, name):
        pass

    @staticmethod
    def verify_root(root):
        if root is None:
            return True
        if type(root) is not CompanyNode.CompanyNode:
            return False
        elif root.get_parent() is not None:
            return False
        return True


def get_tree_dict(node, treeDictionary, currentLevel=1):
    if node is None:
        return {}
    if currentLevel == 1:
        treeDictionary = {currentLevel: [node]}
    childList = node.get_children()
    if len(childList) != 0:
        currentLevel += 1
        if not (currentLevel in treeDictionary):
            treeDictionary[currentLevel] = []
        for child in childList:
            treeDictionary[currentLevel] += [child]
            treeDictionary = get_tree_dict(child, treeDictionary, currentLevel)
    return treeDictionary



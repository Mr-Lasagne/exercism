class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = None
        self.left = None
        self.right = None

    def __str__(self):
        return f"TreeNode(data={self.data}, left={self.left}, right={self.right})"


class BinarySearchTree:
    def __init__(self, tree_data):
        raise NotImplementedError("This method has not been implemented yet.")

    def data(self):
        raise NotImplementedError("This method has not been implemented yet.")

    def sorted_data(self):
        raise NotImplementedError("This method has not been implemented yet.")

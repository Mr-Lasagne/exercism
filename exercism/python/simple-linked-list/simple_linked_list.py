class Node:
    def __init__(self, value):
        raise NotImplementedError("This method has not been implemented yet.")

    def value(self):
        raise NotImplementedError("This method has not been implemented yet.")

    def next(self):
        raise NotImplementedError("This method has not been implemented yet.")


class LinkedList:
    def __init__(self, values=[]):
        raise NotImplementedError("This method has not been implemented yet.")

    def __len__(self):
        raise NotImplementedError("This method has not been implemented yet.")

    def head(self):
        raise NotImplementedError("This method has not been implemented yet.")

    def push(self, value):
        raise NotImplementedError("This method has not been implemented yet.")

    def pop(self):
        raise NotImplementedError("This method has not been implemented yet.")

    def reversed(self):
        raise NotImplementedError("This method has not been implemented yet.")


class EmptyListException(Exception):
    pass

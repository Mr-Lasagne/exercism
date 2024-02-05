class Point:
    def __init__(self, x, y):
        self.x = None
        self.y = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        raise NotImplementedError("This method has not been implemented yet.")

    def search(self, word):
        raise NotImplementedError("This method has not been implemented yet.")

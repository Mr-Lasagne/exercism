class InputCell:
    def __init__(self, initial_value):
        self.value = None


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.value = None

    def add_callback(self, callback):
        raise NotImplementedError("This method has not been implemented yet.")

    def remove_callback(self, callback):
        raise NotImplementedError("This method has not been implemented yet.")

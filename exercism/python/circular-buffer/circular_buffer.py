class BufferFullException(BufferError):
    def __init__(self, message):
        raise NotImplementedError("This method has not been implemented yet.")


class BufferEmptyException(BufferError):
    def __init__(self, message):
        raise NotImplementedError("This method has not been implemented yet.")


class CircularBuffer:
    def __init__(self, capacity):
        raise NotImplementedError("This method has not been implemented yet.")

    def read(self):
        raise NotImplementedError("This method has not been implemented yet.")

    def write(self, data):
        raise NotImplementedError("This method has not been implemented yet.")

    def overwrite(self, data):
        raise NotImplementedError("This method has not been implemented yet.")

    def clear(self):
        raise NotImplementedError("This method has not been implemented yet.")

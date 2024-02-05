import io


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        raise NotImplementedError("This method has not been implemented yet.")

    def __enter__(self):
        raise NotImplementedError("This method has not been implemented yet.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError("This method has not been implemented yet.")

    def __iter__(self):
        raise NotImplementedError("This method has not been implemented yet.")

    def __next__(self):
        raise NotImplementedError("This method has not been implemented yet.")

    def read(self, size=-1):
        raise NotImplementedError("This method has not been implemented yet.")

    @property
    def read_bytes(self):
        raise NotImplementedError("This method has not been implemented yet.")

    @property
    def read_ops(self):
        raise NotImplementedError("This method has not been implemented yet.")

    def write(self, b):
        raise NotImplementedError("This method has not been implemented yet.")

    @property
    def write_bytes(self):
        raise NotImplementedError("This method has not been implemented yet.")

    @property
    def write_ops(self):
        raise NotImplementedError("This method has not been implemented yet.")


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        raise NotImplementedError("This method has not been implemented yet.")

    def __enter__(self):
        raise NotImplementedError("This method has not been implemented yet.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError("This method has not been implemented yet.")

    def recv(self, bufsize, flags=0):
        raise NotImplementedError("This method has not been implemented yet.")

    @property
    def recv_bytes(self):
        raise NotImplementedError("This method has not been implemented yet.")

    @property
    def recv_ops(self):
        raise NotImplementedError("This method has not been implemented yet.")

    def send(self, data, flags=0):
        raise NotImplementedError("This method has not been implemented yet.")

    @property
    def send_bytes(self):
        raise NotImplementedError("This method has not been implemented yet.")

    @property
    def send_ops(self):
        raise NotImplementedError("This method has not been implemented yet.")

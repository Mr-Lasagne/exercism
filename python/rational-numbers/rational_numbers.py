class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = None
        self.denominator = None

    def __eq__(self, other):
        return (
            self.numerator == other.numerator and self.denominator == other.denominator
        )

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        raise NotImplementedError("This method has not been implemented yet.")

    def __sub__(self, other):
        raise NotImplementedError("This method has not been implemented yet.")

    def __mul__(self, other):
        raise NotImplementedError("This method has not been implemented yet.")

    def __truediv__(self, other):
        raise NotImplementedError("This method has not been implemented yet.")

    def __abs__(self):
        raise NotImplementedError("This method has not been implemented yet.")

    def __pow__(self, power):
        raise NotImplementedError("This method has not been implemented yet.")

    def __rpow__(self, base):
        raise NotImplementedError("This method has not been implemented yet.")

"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start) -> None:
        self.start = start
        self.serial_number = start

    def __repr__(self) -> str:
        return (f"SerialGenerator({self.start})")

    def __str__(self):
        return (f"Start value: {self.start}\nCurrent value: {self.serial_number}")

    def generate(self) -> int:
        self.serial_number += 1
        return self.serial_number - 1

    def reset(self) -> None:
        self.serial_number = self.start

s = SerialGenerator(100)
print(repr(s))
print(s)
```python
class Token:
    def __init__(self, symbol, address, volume):
        self.symbol = symbol
        self.address = address
        self.volume = volume

    def __str__(self):
        return f'Token({self.symbol}, {self.address}, {self.volume})'

    def __repr__(self):
        return self.__str__()
```
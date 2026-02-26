class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

c = Calculator()
print(c.add(4, 5))
print(c.add(1, 6, 4))


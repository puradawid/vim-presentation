# How to integrate with Python environment and VIM?

# Is it possible to handle strongly-typed languages as well?

# First thing - debug program!

# Refactor?


class OtherClass:

    def whatever(self, n):
        if n == 0:
            return 0
        anotherValue = n + 2
        return self.whatever(n-1) + anotherValue


OtherClass().whatever(2)

print OtherClass().whatever(100)

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
# Create two Vector objects
vector1 = Vector(3, 4)
vector2 = Vector(1, 2)
vector3 = Vector(12, 12)

# Add two vectors
result_addition = vector1 + vector2
print(f"Addition result: ({result_addition.x}, {result_addition.y})")  # Output: Addition result: (4, 6)

# Subtract two vectors
result_subtraction = vector1 - vector2
print(f"Subtraction result: ({result_subtraction.x}, {result_subtraction.y})")  # Output: Subtraction result: (2, 2)
result_subtraction2 = vector1 - vector3
print(f"Subtraction result: ({result_subtraction2.x}, {result_subtraction2.y})")
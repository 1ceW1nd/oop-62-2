class Notification:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

    def __call__(self):
        print("Notification send")

n = Notification("New message")
print(n)
n()

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2
print(v3.x, v3.y)

print(v1 == v2)

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @classmethod
    def create_admin(cls, name):
        return cls(name, "admin")

admin = User.create_admin("1ceW1nd")
print(admin.name)
print(admin.role)


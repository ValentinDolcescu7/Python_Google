class Coordinate:
    """O coordonata e compusa din valorile x si y"""

    def __init__(self, x, y):
        """Setam valorile x si y"""
        self.x = x
        self.y = y

    def __str__(self):
        """Returnam self ca si string"""
        return f'<{self.x}, {self.y}>'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'<{self.x}, {self.y}>'

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2

        return (x_diff_sq + y_diff_sq) ** 0.5


origin = Coordinate(0, 0)
p = Coordinate(5, 8)
print(origin)
print(p)
print(origin.distance(p))
print(origin == origin)
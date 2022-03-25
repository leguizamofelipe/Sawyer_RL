class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return str(f'{round(self.x,5)},{round(self.y, 5)},{round(self.z, 5)}')

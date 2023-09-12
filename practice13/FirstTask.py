from math import pi


class Sphere:

    def __init__(self, rad=1, x=0, y=0, z=0):
        self.rad = rad
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def get_volume(self):
        return (4/3)*pi*(self.rad**3)

    def get_square(self):
        return 4*pi*(self.rad**2)

    def get_radius(self):
        return self.rad

    def get_center(self):
        return self.x, self.y, self.z

    def set_radius(self, r):
        self.rad = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x1, y1, z1):
        s = (x1**2 + y1**2 + z1**2)**(1/2)
        if s < self.rad:
            return True
        else:
            return False
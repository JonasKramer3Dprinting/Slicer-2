from black import nullcontext
from analythical_geometry import *

class Point_of_level():
    def __init__(self, viewpoint, point, point_a, point_b, id):
        self.triangle_id = id
        self.viewpoint = viewpoint
        self.point = point
        self.point_a = point_a
        self.point_b = point_b
        self.vector_ab = get_difference_vector(self.point_a, self.point_b)

    def get_point_a(self):
        return self.point_a

    def get_point_b(self):
        return self.point_b

    def get_viewpoint(self):
        return self.viewpoint

    def get_point(self):
        return self.point

    def get_vector_ab(self):
        return self.vector_ab

    


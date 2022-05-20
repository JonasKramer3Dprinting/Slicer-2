from analythical_geometry import *

class Triangle():
    def __init__(self, view_point, three_points):
        self.view_point = view_point
        self.point_a = three_points[0]
        self.point_b = three_points[1]
        self.point_c = three_points[2]
        self.vector_ab = get_difference_vector(self.point_a, self.point_b)
        self.vector_ac = get_difference_vector(self.point_a, self.point_c)
        self.vector_bc = get_difference_vector(self.point_b, self.point_c)
        # straight ab starts at point a, so the scalar is 0 for a and 1 for b
        # straight ac starts at point a, so the scalar is 0 for a and 1 for c
        # straight bc starts at point b, so the scalar is 0 for b and 1 for c

    


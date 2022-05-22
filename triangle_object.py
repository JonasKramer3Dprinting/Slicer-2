from black import nullcontext
from analythical_geometry import *

class Triangle():
    def __init__(self, view_point, three_points, id):
        self.triangle_id = id
        self.view_point = view_point
        self.three_points = three_points
        self.point_a = three_points[0]
        self.point_b = three_points[1]
        self.point_c = three_points[2]
        self.vector_ab = get_difference_vector(self.point_a, self.point_b)
        self.vector_ac = get_difference_vector(self.point_a, self.point_c)
        self.vector_bc = get_difference_vector(self.point_b, self.point_c)
        # straight ab starts at point a, so the scalar is 0 for a and 1 for b
        # straight ac starts at point a, so the scalar is 0 for a and 1 for c
        # straight bc starts at point b, so the scalar is 0 for b and 1 for c

    def get_id(self):
        return self.triangle_id

    def get_view_point(self):
        return self.view_point

    def get_all_three_points(self):
        return self.three_points
    
    def get_point_a(self):
        return self.point_a

    def get_point_b(self):
        return self.point_b

    def get_point_c(self):
        return self.point_c

    def get_vector_ab(self):
        return self.vector_ab

    def get_vector_ac(self):
        return self.vector_ac

    def get_vector_bc(self):
        return self.vector_bc

    def get_point_of_level(self, x3, point_a, point_b, vector_ab):
        point = []
        quantity = get_intersection_points_quantity_level_straight(x3, point_a, vector_ab)    
        if not quantity == 1:
            point.append([None, None, None])
        elif quantity ==1:
            scalar, x1, x2= get_scalar_and_point_intersection_level_straight(x3, point_a, vector_ab)
            if scalar > 1 or scalar < 0:
                point.append([None, None, None])
            else:
                point.append([x1, x2, x3])
        point.append(point_a)
        point.append(point_b)
        return point

    def get_all_three_points(self, x3):
        point_ab = self.get_point_of_level(x3, self.point_a, self.point_b, self.vector_ab)
        point_ac = self.get_point_of_level(x3, self.point_a, self.point_c, self.vector_ac)
        point_bc = self.get_point_of_level(x3, self.point_b, self.point_c, self.vector_bc)
        return [point_ab, point_ac, point_bc]

a = Triangle([1,2,1],[[0,0,0],[1,1,2],[2,3,4]],6)

print(a.get_vector_ab())
print(a.get_vector_ac())
print(a.get_vector_bc())

print(a.get_all_three_points(4))

    


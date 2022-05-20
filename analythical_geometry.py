from black import diff


def get_difference_vector(point_e, point_f):
    d_vector = []
    for i in range(0, 3, 1):
        d_vector.append(point_f[i] - point_e[i])
    return d_vector

def get_intersection_points_quantity_level_straight(x3, support_vector, difference_vector):
    s_vec_x3 = support_vector[2]
    d_vec_x3 = difference_vector[2]
    quantity = 1
    if d_vec_x3 == 0 and s_vec_x3 == x3:
        quantity = -1
    elif d_vec_x3 == 0 and not s_vec_x3 == x3:
        quantity = 0
    return quantity

def get_scalar_and_point_intersection_level_straight(x3, support_vector, difference_vector):
    return x3
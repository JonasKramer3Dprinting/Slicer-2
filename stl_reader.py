def read_stl(name):
    vocab_table = []

    connection = open(name, "r")

    content = connection.read()

    lines = content.split("\n")

    triangle_facings = []
    triangle = []

    for line in lines:
        if line.count("facet normal") == 1:
            position = line.find("facet normal")
            numbers = line[(position + 13) : (- 1)]
            number = numbers.split(" ")
            triangle_facings.append(number)
        if line.count("vertex") == 1:
            position = line.find("vertex")
            numbers = line[(position + 9) : (- 1)]
            number = numbers.split(" ")
            triangle.append(number)

    triangles = []
    for i in range(0, len(triangle_facings), 1):
        triangle_list = [triangle[i * 3], triangle[i * 3 + 1], triangle[i * 3 + 2]]
        triangles.append([triangle_facings[i], triangle_list])

    return triangles

def convert_float(float_as_string):
    split = float_as_string.split("e")
    number_float = float(split[0])
    number_exponent = int(split[1])
    number = number_float * 10 ** number_exponent
    return number


def change_float(triangles):
    for triangle in triangles:
        for i in range(0, 3, 1):
            triangle[0][i] = convert_float(triangle[0][i])
            for ii in range(0, 3, 1):
                triangle[1][i][ii] = convert_float(triangle[1][i][ii])
    return triangles

def stl_to_triangles(data_name):
    triangles = read_stl(data_name)
    triangles = change_float(triangles)
    return triangles

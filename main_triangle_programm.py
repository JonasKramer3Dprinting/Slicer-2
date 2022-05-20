from stl_reader import *

triangles = stl_to_triangles("cube.stl")

for line in triangles:
    print(line)
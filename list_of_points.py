from black import nullcontext
from analythical_geometry import *

class List_of_points():
    def __init__(self):
        self.list_of_point_ids = []
        self.list_of_points = []
        self.list_of_point_a = []
        self.list_of_point_b = []
    
    def get_list_of_points(self):
        return self.list_of_points

    def get_all_information_of_point(self, point_id):
        index = self.get_point_index_by_id(point_id)
        all_information = []
        all_information.append(self.get_point(None, index))
        all_information.append(self.get_point_a(None, index))
        all_information.append(self.get_point_b(None, index))

    def get_point(self, point_id, index):
        if index == None:
            index = self.get_point_index_by_id(point_id)
        return self.list_of_points[index]
        
    def get_point_a(self, point_id, index):
        if index == None:
            index = self.get_point_index_by_id(point_id)
        return self.list_of_point_a[index]

    def get_point_b(self, point_id, index):
        if index == None:
            index = self.get_point_index_by_id(point_id)
        return self.list_of_points[index]

    def add_item(self, point, point_a, point_b, point_id):
        self.list_of_points.append(point)
        self.list_of_point_ids.append(point_id)
        self.list_of_point_a.append(point_a)
        self.list_of_point_b.append(point_b)

    def get_point_index_by_id(self, searched_id):
        index = 0
        for id in self.list_of_point_ids:
            if id == searched_id:
                break
            else:
                index = index + 1
        return index

    def remove_item(self, point_id):
        index = self.get_point_index_by_id(point_id)
        self.list_of_point_ids.remove(point_id)
        # get value
        point = self.list_of_points[index]
        point_a = self.list_of_point_a[index]
        point_b = self.list_of_point_b[index]
        # remove by value
        self.list_of_points.remove(point)
        self.list_of_point_a.remove(point_a)
        self.list_of_point_b.remove(point_b)
    
    def print_lists(self):
        print(self.list_of_points)
        print(self.list_of_point_ids)
        print(self.list_of_point_a)
        print(self.list_of_point_b)

    

die_liste = List_of_points()

die_liste.print_lists()

die_liste.add_item([0,0,0],[-1,-1,-1],[1,1,1],0)

die_liste.add_item([1,1,1],[0,0,0],[2,2,2],1)

die_liste.print_lists()

die_liste.remove_item(1)

die_liste.print_lists()

die_liste.remove_item(0)

die_liste.print_lists()
    


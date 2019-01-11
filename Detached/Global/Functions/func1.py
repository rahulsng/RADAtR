# function to display any 2D array/list
def display_2d_list(the_2d_list):
    for each_list in the_2d_list:
        for each_value in each_list:
            print(each_value)
        print()


class class_name:
    def __init__(self, number=None, color=None):
        self.data = number
        self.color = color


my_list = [class_name() for i in range(20)]

for item in my_list:
    print(id(item), type(item))

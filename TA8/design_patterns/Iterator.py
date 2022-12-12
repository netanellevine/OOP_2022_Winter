class ReallySpecialMap:
    def __init__(self):
        self.__map = dict()

    def add(self, key, value):
        self.__map[key] = value

    # We can now iterate over the map data structure

    def __iter__(self):
        return self.__map.__iter__()

    def __getitem__(self, item):
        return self.__map.get(item)


my_map = ReallySpecialMap()
my_map.add(0, 1)
my_map.add(1, 2)
my_map.add(2, 3)
my_map.add(3, 4)
my_map.add(4, 5)
my_map.add(5, 6)

# for key in map:
#     print(map[key])

# We expect to get a custom iterator of the really special map, but we got a normal dictionary iterator.
# We kept the details about the implementation for ourselves.

it = my_map.__iter__()
print(next(it))
print(next(it))
print(next(it))
# # We cannot change a data structure while iterating it
#
my_map.add(6, 7)
print(next(it))

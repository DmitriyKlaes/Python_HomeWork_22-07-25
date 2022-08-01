# Самая далекая планета (текст задачи отдельно в файле)


def find_farthest_orbit(coll):
    from math import pi
    find_s = lambda x: x[0] * x[1] * pi
    max_s = max([find_s(x) for x in coll if x[0] != x[1]])
    result = [x for x in coll if find_s(x) == max_s]
    return result[0]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

# от препода

def find_farthest_orbit(arr):
    return [i for i in arr if i[0] * i[1] == max([i[0] * i[1] for i in arr if i[0] != i[1]])][0]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

def solution062():
    cube_index = {}
    i = 300
    while True:
        i_cube = i * i * i
        cube_key = "".join(sorted(str(i_cube)))
        if cube_key not in cube_index:
            cube_index[cube_key] = [i_cube]
        else:
            cube_index[cube_key].append(i_cube)
            if len(cube_index[cube_key]) == 5:
                return min(cube_index[cube_key])
        i += 1

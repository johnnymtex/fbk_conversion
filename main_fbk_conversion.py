import sys
import convert_fbk_funcs as coords

class Station:
    def __init__(self, name='', N=0, E=0, Z=0):
        self.name = name
        self.N = float(N)
        self.E = float(E)
        self.Z = float(Z)

    def set_height(self, hs):
        self.hs = hs

input_path = sys.argv[1]
output_path = sys.argv[2]

with open(input_path, 'r') as inp_file:
    lines = inp_file.readlines()

initial_stations = []

for line in lines:
    if line[0] == '!':
        continue
    elif line[:3] == 'NEZ':
        sep_line = line.split()
        initial_stations.append(Station(sep_line[1], sep_line[2], sep_line[3], sep_line[4]))

point_list = []

with open(output_path, 'w') as out_file:

    for line in lines:
        point = []

        if line[0] == '!' or line[:3] == 'NEZ' or line[:2] == 'BS':
            continue

        elif line[:3] == 'STN':
            sep_line = line.split()
            id_station = [station.name == sep_line[1] for station in initial_stations]

            if id_station.count(True) == 1:
                current_station = [station for station, is_selected in zip(initial_stations, id_station) if is_selected][0]
                current_station.set_height(float(sep_line[2]))
            else:
                for i in range(len(point_list)):
                    if point_list[i][0] == sep_line[1]:
                        initial_stations.append(Station(point_list[i][0], point_list[i][1], point_list[i][2], point_list[i][3]))
                        current_station = initial_stations[-1]

                        current_station.set_height(float(sep_line[2]))
        
        elif line[:5] == 'PRISM':
            sep_line = line.split()
            hp = float(sep_line[1])

        elif line[:2] == 'F1':
            sep_line = line.split()

            if float(sep_line[4]) == 0:
                continue

            id = sep_line[2]
            print(id, current_station.name, current_station.N, current_station.E)
            N_point, E_point, Z_point = coords.get_NEZ(sep_line[3], sep_line[4], sep_line[5], current_station.N, current_station.E, current_station.Z, current_station.hs, hp)
            comment = sep_line[-1]

            point.append(id)
            point.append(N_point)
            point.append(E_point)
            point.append(Z_point)
            point.append(comment)

            out_file.write(' '.join([id, str(N_point), str(E_point), str(Z_point), comment]))
            out_file.write('\n')

            point_list.append(point)

with open(output_path, 'w') as out_file:
    for i in range(len(point_list)-1, -1, -1):
        out_file.write(','.join([point_list[i][0], str(point_list[i][2]), str(point_list[i][1]), str(point_list[i][3]), point_list[i][4]]))
        out_file.write('\n')
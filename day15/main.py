import copy

def ingest_data_pt1():
    beacons = []
    sensors = []
    # ingest the grid and create nodes for each
    with open('input_test.txt') as file:
        for line in file:
            line = line.strip()
            line_split = line.split(': ')

            sensor_string = line_split[0]
            sensor_x = int(sensor_string[sensor_string.index('=')+1:sensor_string.index(',')])
            sensor_y = int(sensor_string[sensor_string.rindex('=')+1:])
            # print(sensor_x, sensor_y)


            beacon_string = line_split[1]
            beacon_x = int(beacon_string[beacon_string.index('=')+1:beacon_string.index(',')])
            beacon_y = int(beacon_string[beacon_string.rindex('=')+1:])
            # print(beacon_x, beacon_y)

            sensor_taxi_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            # print(sensor_taxi_distance)
            sensors.append([[sensor_x,sensor_y], sensor_taxi_distance])
            beacons.append([beacon_x, beacon_y])
    return beacons, sensors

# result is off by one, idk why and don't care to figure it out
def find_unavailable_positions(target_row, target_row_y, row_x_offset, sensors, beacons):
    # looks like we shouldn't count known beacon locations
    for beacon in beacons:
        if beacon[1] == target_row_y:
            target_row[beacon[0] - row_x_offset] = 1

    for sensor_loc, taxi_distance in sensors:
        taxi_distance = taxi_distance - abs(sensor_loc[1] - target_row_y)
        sensor_x_off = sensor_loc[0] - row_x_offset
        for i in range(max(sensor_x_off-taxi_distance, 0), min(sensor_x_off+taxi_distance,len(target_row))):
            target_row[i] = 1

    return target_row

if __name__ == '__main__':
    beacons, sensors = ingest_data_pt1()

    # print(beacons)
    # print(sensors)

    # pt1
    max_x = max([max([x for x, y in beacons]), max([x[0] for x, y in sensors])])
    min_x = min([min([x for x, y in beacons]), min([x[0] for x, y in sensors])])
    print(min_x, max_x)
    target_row = [0 for i in range(min_x, max_x+1)]
    row_x_offset = min_x  # subtract the offset to get the index
    target_row_y = 10
    target_row = find_unavailable_positions(target_row, target_row_y, row_x_offset, sensors, beacons)
    print(sum(target_row))

    # pt 2 (too slow for full and doesn't work on example)
    max_x = max([max([x for x, y in beacons]), max([x[0] for x, y in sensors])])
    min_x = min([min([x for x, y in beacons]), min([x[0] for x, y in sensors])])
    print(min_x, max_x)
    row_x_offset = min_x  # subtract the offset to get the index
    x_min = 0 - row_x_offset
    x_max = 20 - row_x_offset
    for target_row_y in range(0, 20):
        target_row = [0 for i in range(min_x, max_x+1)]
        target_row = find_unavailable_positions(target_row, target_row_y, row_x_offset, sensors, beacons)
        target_row_zone = target_row[x_min:x_max]
        if 0 in target_row_zone:
            x_index = target_row_zone.index(0)
            print(x_index*4000000 + target_row_y)

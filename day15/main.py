import copy

def ingest_data_pt1():
    beacons = []
    sensors = []
    # ingest the grid and create nodes for each
    with open('input.txt') as file:
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

def find_unavailable_positions_pt1(target_row, target_row_y, row_x_offset, sensors, beacons):

    for sensor_loc, taxi_distance in sensors:
        taxi_distance = taxi_distance - abs(sensor_loc[1] - target_row_y)
        sensor_x_off = sensor_loc[0] - row_x_offset
        for i in range(max(sensor_x_off-taxi_distance, 0), min(sensor_x_off+taxi_distance,len(target_row))):
            target_row[i] = 1

    return target_row


def find_unavailable_positions_pt2(target_row_y, row_x_offset, sensors, beacons, x_lim):
    spaces_covered = []
    for sensor_loc, taxi_distance in sensors:
        # print(sensor_loc, taxi_distance, target_row_y)
        taxi_distance = taxi_distance - abs(sensor_loc[1] - target_row_y)
        # print(taxi_distance)
        sensor_x_off = sensor_loc[0] - row_x_offset
        if taxi_distance >= 0:
            spaces_covered.append([sensor_x_off - taxi_distance, sensor_x_off + taxi_distance])

    # print(spaces_covered)
    spaces_covered.sort(key=lambda x: x[0])
    # print(spaces_covered)

    last_covered = max(0 - row_x_offset, spaces_covered[0][1])
    for i in range(1, len(spaces_covered)):
        space = spaces_covered[i]
        # print(space, last_covered)
        if last_covered < space[0] - 1 and [last_covered + 1 + row_x_offset, target_row_y] not in beacons:
            return last_covered + 1 + row_x_offset
        if last_covered < space[1]:
            last_covered = space[1]
        if last_covered > x_lim:
            return None

if __name__ == '__main__':
    beacons, sensors = ingest_data_pt1()

    # print(beacons)
    # print(sensors)

    # pt1
    max_x = max([max([x for x, y in beacons]), max([x[0] for x, y in sensors])])
    min_x = min([min([x for x, y in beacons]), min([x[0] for x, y in sensors])])
    # print(min_x, max_x)
    target_row = [0 for i in range(min_x, max_x+1)]
    row_x_offset = min_x  # subtract the offset to get the index
    target_row_y = 10
    target_row = find_unavailable_positions_pt1(target_row, target_row_y, row_x_offset, sensors, beacons)
    # print(sum(target_row))

    # pt 2 (too slow for full and doesn't work on example)
    max_x = max([max([x for x, y in beacons]), max([x[0] for x, y in sensors])])
    min_x = min([min([x for x, y in beacons]), min([x[0] for x, y in sensors])])
    # print(min_x, max_x)
    row_x_offset = min_x  # subtract the offset to get the index
    x_lim = 4000000
    x_min = 0 - row_x_offset
    x_max = x_lim - row_x_offset
    for target_row_y in range(0, x_lim + 1):
        target_row = find_unavailable_positions_pt2(target_row_y, row_x_offset, sensors, beacons, x_lim)
        if target_row is not None:
            print(target_row, target_row_y, target_row*4000000 + target_row_y)
        # break

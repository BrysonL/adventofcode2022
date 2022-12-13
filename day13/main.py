import copy
from functools import cmp_to_key

def ingest_data_pt1():
    signal_pairs = []
    left_values = None
    right_values = None
    # ingest the grid and create nodes for each
    with open('input.txt') as file:
        for line in file:
            line = line.strip()
            if line == '':
                signal_pairs.append([left_values, right_values])
                left_values = None
                right_values = None
                continue

            # only 2 digit number is 10, this lets me id it without funky index incrementing logic
            line = line.replace('10', 'z')

            level = -1
            current_lists = []

            for i in range(len(line)):
                char = line[i]
                if char == '[':  # start a new list
                    level += 1
                    if level <= len(current_lists):
                        current_lists.append([])

                    # don't think i need this whole loop, just the first iteration
                    # but i added while debugging and am afraid to remove
                    for j in range(level, len(current_lists)):
                        current_lists[j] = []
                    current_item = current_lists[level]
                    # print('level up', current_item)
                    continue  # continue not really needed, no other ifs will be satisfied
                elif char == ']':  # the previous list is finished
                    level -= 1
                    # if we're closing the last parenthesis, we don't need to modify the last item
                    # this was a bug i had for a while because Python is nice
                    # and lets me use negative indicies without error
                    if level > -1:
                        current_item = current_lists[level]
                        # print('level down', current_item)
                        # if len(current_lists[level + 1]) > 0 and isinstance(current_lists[level + 1][0], list):
                        current_item.append(copy.deepcopy(current_lists[level + 1]))
                        # print(current_item)
                    continue

                elif char.isnumeric():
                    current_item.append(int(char))
                    # print('lists', current_lists)
                elif char == 'z':
                    current_item.append(10)

            # format the list in the same way as the file line to make visual comparison easier
            list_str = str(current_lists[0]).replace(' ','').replace('10','z')

            # check to make sure the lines match
            if line != list_str:
                print('lines don\'t match')
                print(list_str)
                print(line)
                print()
            if left_values is None:
                left_values = current_lists[0]
            else:
                right_values = current_lists[0]

        signal_pairs.append([left_values, right_values])

    return signal_pairs

def ingest_data_pt2():
    packets = []
    # ingest the grid and create nodes for each
    with open('input.txt') as file:
        for line in file:
            line = line.strip()
            if line == '':
                continue

            # only 2 digit number is 10, this lets me id it without funky index incrementing logic
            line = line.replace('10', 'z')

            level = -1
            current_lists = []

            for i in range(len(line)):
                char = line[i]
                if char == '[':  # start a new list
                    level += 1
                    if level <= len(current_lists):
                        current_lists.append([])

                    # don't think i need this whole loop, just the first iteration
                    # but i added while debugging and am afraid to remove
                    for j in range(level, len(current_lists)):
                        current_lists[j] = []
                    current_item = current_lists[level]
                    # print('level up', current_item)
                    continue  # continue not really needed, no other ifs will be satisfied
                elif char == ']':  # the previous list is finished
                    level -= 1
                    # if we're closing the last parenthesis, we don't need to modify the last item
                    # this was a bug i had for a while because Python is nice
                    # and lets me use negative indicies without error
                    if level > -1:
                        current_item = current_lists[level]
                        # print('level down', current_item)
                        # if len(current_lists[level + 1]) > 0 and isinstance(current_lists[level + 1][0], list):
                        current_item.append(copy.deepcopy(current_lists[level + 1]))
                        # print(current_item)
                    continue

                elif char.isnumeric():
                    current_item.append(int(char))
                    # print('lists', current_lists)
                elif char == 'z':
                    current_item.append(10)

            # format the list in the same way as the file line to make visual comparison easier
            list_str = str(current_lists[0]).replace(' ','').replace('10','z')

            # check to make sure the lines match
            if line != list_str:
                print('lines don\'t match')
                print(list_str)
                print(line)
                print()
            packets.append(current_lists[0])

    return packets

def pair_ordered(left_value, right_value):
    if isinstance(left_value, int) and isinstance(right_value, int):  # both ints, compare
        if left_value < right_value:
            return True
        elif left_value > right_value:
            return False
        else:
            return None
    elif isinstance(right_value, int):  # right only int, make right list and compare
        return pair_ordered(left_value, [right_value])
    elif isinstance(left_value, int):  # left only int, make left list and compare
        return pair_ordered([left_value], right_value)

    # now we can assume that left and right are both lists
    for i in range(min(len(left_value), len(right_value))):
        result = pair_ordered(left_value[i], right_value[i])
        if result is not None:
            return result

    if len(right_value) < len(left_value):  # left should be longer than right
        return False
    elif len(right_value) > len(left_value):  # left should be longer than right
        return True
    else:
        return None


def compare(left, right):
    res = pair_ordered(left, right)
    if res:
        return -1
    else:
        return 1


if __name__ == '__main__':
    signal_pairs = ingest_data_pt1()

    score = 0
    for i in range(len(signal_pairs)):
        pair = signal_pairs[i]
        # print(pair[0])
        # print(pair[1])
        if pair_ordered(pair[0], pair[1]):
            # print('pair ordered: ', i+1)
            score += i+1
        else:
            pass
            # print('pair not ordered: ', i+1)

    print(score)

    packets = ingest_data_pt2()
    packets.append([[2]])
    packets.append([[6]])

    sorted_packets = sorted(packets, key=cmp_to_key(compare))

    start_index = sorted_packets.index([[2]]) + 1
    end_index = sorted_packets.index([[6]]) + 1
    print(start_index * end_index)

    # for packet in sorted_packets:
        # print(packet)
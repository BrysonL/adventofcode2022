def ingest_data_pt1():
    # each row has two comma sep ranges defined by a hyphen
    groupings = []
    with open("input.txt") as file:
        for line in file:
            line = line.strip()

            first_split = line.split(',')

            elf1_split = first_split[0].split('-')
            elf2_split = first_split[1].split('-')

            groupings.append([elf1_split, elf2_split])

    return groupings

def count_complete_overlaps(groupings):
    # figure out for which groupings one completely overlaps another
    score = 0

    for group in groupings:
        # calc the min/max of each range
        elf1_min = int(group[0][0])
        elf1_max = int(group[0][1])

        elf2_min = int(group[1][0])
        elf2_max = int(group[1][1])

        # if the max and min of one elf are completely within the max and min of the other elf, increment score
        if (elf1_min <= elf2_min and elf1_max >= elf2_max) or (elf1_min >= elf2_min and elf1_max <= elf2_max):
            score += 1

    return score

def count_any_overlaps(groupings):
    # same as above, except look for any overlap
    score = 0

    for group in groupings:
        elf1_min = int(group[0][0])
        elf1_max = int(group[0][1])

        elf2_min = int(group[1][0])
        elf2_max = int(group[1][1])

        # overlap exists if either of the maxes are within the range of the other
        if (elf2_min <= elf1_max <= elf2_max) or (elf1_min <= elf2_max <= elf1_max):
            score += 1

    return score


if __name__ == '__main__':
    groupings = ingest_data_pt1()

    print(count_any_overlaps(groupings))





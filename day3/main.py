def ingest_data_pt1():
    # each elf has a sack that should be split in half into two sacks
    sacks = []
    with open("input.txt") as file:
        for line in file:
            line = line.strip()

            sack_size = int(len(line) / 2)  # lines guaranteed to be ints

            sack_1 = line[0:sack_size]
            sack_2 = line[sack_size:]

            sacks.append([sack_1, sack_2])

    return sacks

def ingest_data_pt2():
    # now each group of sacks should be three lines
    sacks = []
    with open("input.txt") as file:
        index = 0
        group = []
        for line in file:
            line = line.strip()

            group.append(line)  # add each line to the group
            index += 1

            if index == 3:  # if we have three items (could also do len(group)), add to the list and reset tally
                print(group)
                sacks.append(group)
                index = 0
                group = []

    return sacks

def score_value(character):
    # figure out the score of each character
    if ord(character) >= 97:  # this means lower case
        return ord(character) - 96  # scoring given in prompt
    else:  # this means upper case
        return ord(character) - 38

def compare_sack(sack):
    # find the first char that appears in both sacks
    sack_1 = sack[0]
    sack_2 = sack[1]

    print(sack_1)
    print(sack_2)

    for character in sack_1:
        if character in sack_2:
            print(character)
            return character

    return None

def compare_group(group):
    # find the first char that appears in all three sacks
    sack_1 = group[0]
    sack_2 = group[1]
    sack_3 = group[2]

    for character in sack_1:
        if character in sack_2 and character in sack_3:
            return character

if __name__ == '__main__':
    sacks = ingest_data_pt2()

    priority = 0

    # sum the "priority" of the first shared value in each sack/group

    # for sack in sacks:
    #     priority += score_value(compare_sack(sack))
    #
    # print(priority)

    for sack in sacks:
        priority += score_value(compare_group(sack))

    print(priority)





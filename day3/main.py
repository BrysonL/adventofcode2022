

def ingest_data_pt1():
    sacks = []
    with open("input.txt") as file:
        for line in file:
            line = line.strip()

            sack_size = int(len(line) / 2)

            sack_1 = line[0:sack_size]
            sack_2 = line[sack_size:]

            sacks.append([sack_1, sack_2])

    return sacks

def ingest_data_pt2():
    sacks = []
    with open("input.txt") as file:
        index = 0
        group = []
        for line in file:
            line = line.strip()

            group.append(line)
            index += 1

            if index == 3:
                print(group)
                sacks.append(group)
                index = 0
                group = []

    return sacks

def score_value(character):
    if ord(character) >= 97:
        return ord(character) - 96
    else:
        return ord(character) - 38

def compare_sack(sack):
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
    sack_1 = group[0]
    sack_2 = group[1]
    sack_3 = group[2]

    for character in sack_1:
        if character in sack_2 and character in sack_3:
            return character

if __name__ == '__main__':
    sacks = ingest_data_pt2()

    priority = 0

    # for sack in sacks:
    #     priority += score_value(compare_sack(sack))
    #
    # print(priority)

    for sack in sacks:
        priority += score_value(compare_group(sack))

    print(priority)





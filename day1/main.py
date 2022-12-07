def ingest_data():
    # each elf has a bag (array) of food where each food has a calorie value (values)
    elf_carry = [[]]
    with open("input.txt") as file:
        i = 0
        for line in file:
            if line == '\n':  # a new line means the bag is done
                i += 1
                elf_carry.append([])  # add the bag for the next elf
            else:  # if not a bag, append the calorie value for the food
                elf_carry[i].append(int(line))
    return elf_carry


def calc_max_carry(elf_carry):
    max_carry = 0
    for elf in elf_carry:
        elf_tot = sum(elf)  # each bag is an array of ints so we can sum it
        if elf_tot > max_carry:  # if this is the biggest bag we've seen, update the max
            max_carry = elf_tot

    return max_carry


def calc_top_three_carry(elf_carry):
    # this is sub optimal, probably should sum all sub-arrays, sort array, sum top three
    max_carry = 0
    second_carry = 0
    third_carry = 0

    for elf in elf_carry:
        elf_tot = sum(elf)
        if elf_tot > max_carry:  # each time we update one of the maxes we need to bump the previous max values down
            third_carry = second_carry
            second_carry = max_carry
            max_carry = elf_tot
        elif elf_tot > second_carry:
            third_carry = second_carry
            second_carry = elf_tot
        elif elf_tot > third_carry:
            third_carry = elf_tot

    return max_carry + second_carry + third_carry


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #pt1
    print(calc_max_carry(ingest_data()))

    #pt2
    print(calc_top_three_carry(ingest_data()))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

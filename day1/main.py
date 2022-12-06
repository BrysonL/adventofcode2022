# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def ingest_data():
    elf_carry = [[]]
    with open("input.txt") as file:
        i = 0
        for line in file:
            if line == '\n':
                i += 1
                elf_carry.append([])
            else:
                elf_carry[i].append(int(line))
    return elf_carry

def calc_max_carry(elf_carry):
    max_carry = 0
    for elf in elf_carry:
        elf_tot = sum(elf)
        if elf_tot > max_carry:
            max_carry = elf_tot

    return max_carry

def calc_top_three_carry(elf_carry):
    max_carry = 0
    second_carry = 0
    third_carry = 0

    for elf in elf_carry:
        elf_tot = sum(elf)
        if elf_tot > max_carry:
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
    print(calc_max_carry(ingest_data()))

    print(calc_top_three_carry(ingest_data()))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

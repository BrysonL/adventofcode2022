def ingest_data_pt1():
    instructions = [1]
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            if line == 'noop':
                instructions.append(0)
            else:
                instructions.append(0)
                instructions.append(int(line.split(' ')[1]))

    return instructions

def calc_signal_strength_pt1(instuctions, cycles):
    total_strength = 0
    for cycle in cycles:
        total_strength += cycle * sum(instructions[:cycle])

    return total_strength

def draw_letters(instructions):
    screen = []
    current_row = []
    sprite_center = 0
    CRT_row_loc = 0
    for instruction in instructions:
        sprite_center += instruction
        if abs(sprite_center - CRT_row_loc) < 2:
            current_row.append('#')
        else:
            current_row.append('.')

        CRT_row_loc += 1
        if CRT_row_loc == 40:
            CRT_row_loc = 0
            screen.append(current_row)
            current_row = []

    return screen


if __name__ == '__main__':
    instructions = ingest_data_pt1()
    cycles = [20, 60, 100, 140, 180, 220]

    total_strength = calc_signal_strength_pt1(instructions, cycles)
    print(total_strength)

    screen = draw_letters(instructions)
    for row in screen:
        print(' '.join(row))
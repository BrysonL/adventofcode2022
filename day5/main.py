

def ingest_data_pt1():
    stacks = [[] for i in range(9)]
    instructions = []

    with open("input.txt") as file:
        for line in file:
            if line[0] == '[':
                for i in range(9):
                    item_let = line[i*4 + 1]
                    if item_let != ' ':
                        stacks[i].append(item_let)

            if line[0] == 'm':
                line = line.strip()
                line = line[5:]

                num_move = int(line[:line.index(' ')])
                line = line[line.index(' ')+1:]

                to_stack = int(line[line.rindex(' ')+1:])
                line = line[:line.rindex(' ')]

                from_stack = int(line[line.index(' ')+1:line.rindex(' ')])

                instructions.append([num_move, to_stack, from_stack])

    for stack in stacks:
        stack.reverse()

    return stacks, instructions

def process_stacks_pt1(stacks, instructions):
    for instruction in instructions:
        num_move, to_stack, from_stack = instruction
        for i in range(num_move):
            stacks[to_stack-1].append(stacks[from_stack-1].pop())

    return stacks

def process_stacks_pt2(stacks, instructions):
    for instruction in instructions:
        num_move, to_stack, from_stack = instruction
        items_to_move = stacks[from_stack-1][len(stacks[from_stack-1])-num_move:]

        print(items_to_move)
        stacks[from_stack - 1] = stacks[from_stack-1][:len(stacks[from_stack - 1]) - num_move]

        for item in items_to_move:
            stacks[to_stack-1].append(item)

    return stacks

if __name__ == '__main__':
    test1 = ['a', 'b', 'c']

    print(test1)
    test1.reverse()
    print(test1)
    print(test1.pop())
    print(test1)

    stacks, instructions = ingest_data_pt1()

    stacks = process_stacks_pt2(stacks, instructions)

    for stack in stacks:
        print(stack.pop())




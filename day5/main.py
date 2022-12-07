def ingest_data_pt1():
    # build some stacks, then do some stack operations on them
    # probably could have built a class for this...
    stacks = [[] for i in range(9)]
    instructions = []

    with open("input.txt") as file:
        for line in file:
            # lucky for me, the first stack is the tallest, so to determine if it is a stack check the first char
            if line[0] == '[':
                for i in range(9):  # there are 9 stacks in my file (also lucky/planned)
                    item_let = line[
                        i * 4 + 1]  # each stack's contents is exactly one char, and 4 chars from the previous

                    # not all stacks are the same fullness, skip ones that don't have items this level
                    if item_let != ' ':
                        stacks[i].append(item_let)

            if line[0] == 'm':  # this means line is an instruction
                line = line.strip()  # get rid of pesky new line
                line = line[5:]  # take out "move "

                # from the beginning of the string to the first space is the number of items to move from the stack
                num_move = int(line[:line.index(' ')])

                line = line[line.index(' ') + 1:]  # now chop off the first number

                # the stack to go to is the substring from the last space to the end
                to_stack = int(line[line.rindex(' ') + 1:])
                line = line[:line.rindex(' ')]  # now chop off the last number

                # the stack to take from is the number left in the middle of the remaining spaces
                from_stack = int(line[line.index(' ') + 1:line.rindex(' ')])

                # store the instruction in the instruction list
                instructions.append([num_move, to_stack, from_stack])

    # I added from top down, but stacks go bottom up so reverse the order
    for stack in stacks:
        # don't remember what this is called, but it directly modifies the array, not just returning a result
        # so we don't need to store the result anywhere
        stack.reverse()

    return stacks, instructions


def process_stacks_pt1(stacks, instructions):
    # for each instruction, pop the right number of items from the stacks and move them
    for instruction in instructions:
        num_move, to_stack, from_stack = instruction
        for i in range(num_move):
            # minus one stack index since python is zero-indexed
            stacks[to_stack - 1].append(stacks[from_stack - 1].pop()) # this combo reverses order for pt 1

    return stacks


def process_stacks_pt2(stacks, instructions):
    # same as above but preserve order
    # note: if I had built a stack class, could have popped the boxes to move to a new stack
    # then popped that stack to the target

    for instruction in instructions:
        num_move, to_stack, from_stack = instruction

        # compute the list of items you're supposed to move
        items_to_move = stacks[from_stack - 1][len(stacks[from_stack - 1]) - num_move:]

        # now remove those items from the original stack
        stacks[from_stack - 1] = stacks[from_stack - 1][:len(stacks[from_stack - 1]) - num_move]

        # and append them to the new stacks
        for item in items_to_move:
            # note: for iterates from front to back of list, so order is preserved.
            stacks[to_stack - 1].append(item)

    return stacks


if __name__ == '__main__':
    # remeber what the python array functions do
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

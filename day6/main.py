import copy

def ingest_data_pt1():
    # today is one giant string on a single line
    sequence = ""

    with open("input.txt") as file:
        for line in file:
            sequence = line.strip()

    return sequence

def find_first_marker_pt1(sequence):
    # pt1 easy to brute force, make sure none of the chars in the most recent 4 repeat
    for i in range(3, len(sequence)):
        if sequence[i] not in sequence[i-3:i]\
                and sequence[i-1] not in sequence[i-3:i-1]\
                and sequence[i-2] not in sequence[i-3:i-2]:
            return i + 1  # add one to total because python is zero indexed but answer is one indexed

def find_first_marker_pt2(sequence, length):
    # little harder, figure out if a string of 14 chars has any repeats
    # there's probably a builtin for this but i didn't look very hard

    # make an array to track all the times we've seen a char
    last_appearance = {}

    for i in range(len(sequence)):
        # there are def smarter ways to do this, but...

        # find the char of interest
        new_char = sequence[i]

        if i >= length:
            # for the string of length we care about, figure out if any of the characters are in the string twice
            start_of_packet = i-length

            return_bool = True

            # for each character, figure out the last time we saw it (besides right now)
            for j in range(i-length, i+1):
                char = sequence[j]
                # print(j)
                if char in last_appearance:
                    # deep copy the array because apparently python arrays are stored by memory location or whatever.
                    # if you don't do this you modify the array in the dict too and stuff breaks.
                    array = copy.deepcopy(last_appearance[char])

                    # remove the latest value, which is the char we're looking at if there are no other instances in str
                    array.pop()

                    # if we have seen this letter besides right now, and we've seen it since the start of the string
                    # there are repeats, don't return
                    if len(array) > 0 and array.pop() >= start_of_packet:
                        # print("breaking ", i)
                        return_bool = False
                        break

            # if we didn't see any duplicates, return
            if return_bool:
                return i

        # add this instance of the character to our tracker
        if new_char in last_appearance:
            last_appearance[new_char].append(i)
        else:
            last_appearance[new_char] = [i]

if __name__ == '__main__':
    sequence = ingest_data_pt1()

    print(find_first_marker_pt2(sequence, 14))



import copy

def ingest_data_pt1():
    sequence = ""

    with open("input.txt") as file:
        for line in file:
            sequence = line.strip()

    return sequence

def find_first_marker_pt1(sequence):
    for i in range(3, len(sequence)):
        if sequence[i] not in sequence[i-3:i]\
                and sequence[i-1] not in sequence[i-3:i-1]\
                and sequence[i-2] not in sequence[i-3:i-2]:
            return i + 1

def find_first_marker_pt2(sequence, length):
    last_appearance = {}

    for i in range(len(sequence)):
        new_char = sequence[i]

        if i >= length:
            start_of_packet = i-length

            return_bool = True
            for j in range(i-length, i+1):
                char = sequence[j]
                print(j)
                if char in last_appearance:
                    array = copy.deepcopy(last_appearance[char])
                    array.pop()
                    if len(array) > 0 and array.pop() >= start_of_packet:
                        print("breaking ", i)
                        return_bool = False
                        break

            if return_bool:
                return i

        if new_char in last_appearance:
            last_appearance[new_char].append(i)
        else:
            last_appearance[new_char] = [i]

if __name__ == '__main__':
    sequence = ingest_data_pt1()

    print(find_first_marker_pt2(sequence, 14))



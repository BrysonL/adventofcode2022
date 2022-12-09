def ingest_data_pt1():
    grid = []
    with open("input.txt") as file:
        for line in file:
            line = line.strip().split(' ')


if __name__ == '__main__':
    grid, instructions, starting_pos = ingest_data_pt1()

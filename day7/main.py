import copy

class File:
    def __init__(self, name, size, parent_dir=None):
        self.size = size
        self.name = name
        self.parent_dir = parent_dir

    def get_size(self):
        return self.size

    def __str__(self):
        return self.name + ' ' + str(self.size)

class Directory:
    def __init__(self, name, parent_dir=None):
        self.files = []
        self.name = name
        self.parent_dir = parent_dir

    def add_file(self, file):
        self.files.append(file)

    def calc_size(self):
        size = 0
        for file in self.files:
            if isinstance(file, Directory):
                size += file.calc_size()
            elif isinstance(file, File):
                size += file.get_size()

        return size

    def get_sizes(self):
        sizes = [[self, self.calc_size()]]
        for file in self.files:
            if isinstance(file, File):
                continue

            sizes.append([file.name, file.calc_size()])
            for size in file.get_sizes():
                sizes.append(size)

        return sizes

    def get_parent_dir(self):
        return self.parent_dir

    def __str__(self):
        string = self.name + '\n'
        for file in self.files:
            string += '\t' + str(file)

        return string

def ingest_data_pt1():
    root_dir = Directory('/')
    current_dir = root_dir

    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            if line == '$ cd /':
                continue

            if line[0] == '$':
                if line[0:4] == '$ cd':
                    #change dir
                    if line[-2:] == '..':
                        #go up
                        # print('going up', current_dir)
                        current_dir = current_dir.get_parent_dir()
                        # print('went up', current_dir)
                        # print()

                    else:
                        # print('old dir', current_dir)
                        dir = line[line.rindex(' ') + 1:]
                        new_dir = Directory(dir, current_dir)
                        current_dir.add_file(new_dir)
                        current_dir = new_dir
                        # print('new dir', current_dir)
                        # print()

                elif line[0:4] == "$ ls":
                    # do nothing on list
                    continue

            elif line[0:3] == 'dir':
                # do nothing on ls dir
                continue

            else: #item is a file
                split_line = line.split(' ')
                size = int(split_line[0])
                name = split_line[1]

                new_file = File(name, size, current_dir)
                current_dir.add_file(new_file)
                print(current_dir.calc_size())

    return root_dir


if __name__ == '__main__':
    root_dir = ingest_data_pt1()
    # print(root_dir)
    # print(root_dir.calc_size())
    tot = 0
    sizes = root_dir.get_sizes()

    tot_size = root_dir.calc_size()
    avail_size = 70000000 - tot_size
    needed_size = 30000000 - avail_size
    min_needed = 30000000
    print(sizes)
    for size in sizes:
        if size[1] < 100000:
            tot += size[1]

        if size[1] > needed_size and size[1] < min_needed:
            min_needed = size[1]

    # print(tot / 2)

    print(needed_size, min_needed)



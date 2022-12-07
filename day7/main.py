# #babysFirstClass
class File:
    # a file has a name, size, and parent directory
    # can also be thought of as a leaf in a tree
    # they don't really do much

    def __init__(self, name, size, parent_dir=None):
        self.size = size
        self.name = name
        self.parent_dir = parent_dir

    def get_size(self):
        return self.size

    def __str__(self):
        return self.name + ' ' + str(self.size)

class Directory:
    # a directory is a branch in a tree and contains multiple links to other files or directories

    def __init__(self, name, parent_dir=None):
        self.files = []
        self.name = name
        self.parent_dir = parent_dir

    def add_file(self, file):
        # this file can be a File or Directory object but #yolo so no type checking
        self.files.append(file)

    def calc_size(self):
        size = 0
        for file in self.files:
            # if this file in the directory is a directory, recursively calc the size
            if isinstance(file, Directory):
                size += file.calc_size()

            # if this file in the directory is a File, add the size to the total
            elif isinstance(file, File):
                size += file.get_size()

        return size

    def get_sizes(self):
        # make a list of the sizes of all Directories in this directory
        sizes = []
        for file in self.files:
            # we only want directory sizes, skip files
            if isinstance(file, File):
                continue

            # for each directory, add this directory's size
            sizes.append([file.name, file.calc_size()])

            # for each file in that directory, also get the sizes
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
    # build the file tree from the input
    root_dir = Directory('/')
    current_dir = root_dir

    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            # skip the first line (this would happen anyway since it doesn't fit any other cases but this is clearer)
            if line == '$ cd /':
                continue

            if line[0] == '$':  # if this is a command
                if line[0:4] == '$ cd':
                    #change dir
                    if line[-2:] == '..':
                        # go up to parent
                        # print('going up', current_dir)
                        current_dir = current_dir.get_parent_dir()
                        # print('went up', current_dir)
                        # print()

                    else:
                        # go down to new dir
                        # print('old dir', current_dir)
                        dir = line[line.rindex(' ') + 1:]
                        new_dir = Directory(dir, current_dir)
                        current_dir.add_file(new_dir)
                        current_dir = new_dir
                        # print('new dir', current_dir)
                        # print()

                elif line[0:4] == "$ ls":  # do nothing on list
                    continue

            elif line[0:3] == 'dir':  # do nothing on dir result from ls
                continue

            else:  # item is a file, figure out name and size
                split_line = line.split(' ')
                size = int(split_line[0])
                name = split_line[1]

                # make new file and add to current dir
                new_file = File(name, size, current_dir)
                current_dir.add_file(new_file)
                # print(current_dir.calc_size())

    return root_dir


if __name__ == '__main__':
    root_dir = ingest_data_pt1()
    # print(root_dir)
    # print(root_dir.calc_size())
    tot = 0
    sizes = root_dir.get_sizes()

    # figure out how much space is left
    tot_size = root_dir.calc_size()
    avail_size = 70000000 - tot_size

    # figure out the min space needed to be freed
    needed_size = 30000000 - avail_size
    min_needed = 30000000

    # print(sizes)
    for size in sizes:
        # pt1 - sum sizes less than 100k
        if size[1] < 100000:
            tot += size[1]

        # pt2 - find the minimum size that also frees enough space
        if size[1] > needed_size and size[1] < min_needed:
            min_needed = size[1]

    print(tot)

    print(needed_size, min_needed)



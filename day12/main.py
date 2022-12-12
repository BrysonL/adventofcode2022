class Node:
    def __init__(self, elevation, id):
        self.elevation = elevation
        self.id = id
        self.adjacent_nodes = []

    def add_adjacent_node(self, node):
        height_dif = node.elevation - self.elevation
        if  height_dif <= 1:
            self.adjacent_nodes.append(node)

    def __str__(self):
        return self.id

def calc_elevation(char):
    return ord(char)-96

def ingest_data_pt1():
    node_grid = []
    start_node = None
    possible_starts = []
    # ingest the grid and create nodes for each
    with open('input.txt') as file:
        for line in file:
            line = line.strip()
            node_grid_row = []
            for char in line:
                if char == 'E':
                    elevation = calc_elevation('z')
                elif char == 'S':
                    elevation = calc_elevation('a')
                else:
                    elevation = calc_elevation(char)
                node_grid_row.append(Node(elevation, char))
            node_grid.append(node_grid_row)

    # add adjacent nodes in the rows
    num_cols = len(node_grid)
    num_rows = len(node_grid[0])
    for j in range(num_cols):  # j = row number
        for i in range(num_rows):  # i = column number
            node = node_grid[j][i]
            if node.id == 'S':
                start_node = node
                possible_starts.append(node)
            if node.id == 'a':
                possible_starts.append(node)

            # I misread the prompt and initially had diagonal moves, too... RIP...
            # add adjacent nodes for all of the nodes in the graph next to this one
            if j != num_cols - 1:  # don't go down on last row
                # if i != 0:  # don't go left on first col
                #     node.add_adjacent_node(node_grid[j+1][i-1])
                node.add_adjacent_node(node_grid[j+1][i])

                # if i != num_rows - 1:  # don't go right on last col
                #     node.add_adjacent_node(node_grid[j+1][i+1])

            if i != 0:
                node.add_adjacent_node(node_grid[j][i-1])
            if i != num_rows - 1:
                node.add_adjacent_node(node_grid[j][i+1])

            if j != 0:  # top row, don't go up but still go down
                # if i != 0:
                #     node.add_adjacent_node(node_grid[j-1][i-1])

                node.add_adjacent_node(node_grid[j-1][i])

                # if i != num_rows - 1:
                #     node.add_adjacent_node(node_grid[j-1][i+1])

    return node_grid, start_node, possible_starts


def find_path_to_end(start_node):
    visited_nodes = {}
    tentative_visits = {start_node: 0}
    while True:
        # if we can't get to the end, return a high number
        if len(tentative_visits) == 0:
            return 1000000

        current_node = min(tentative_visits, key=tentative_visits.get)
        dist_to_start = tentative_visits[current_node]
        print(len(visited_nodes), len(tentative_visits), str(current_node), dist_to_start)
        for node in current_node.adjacent_nodes:
            if node.id == 'E':
                return dist_to_start + 1
            elif node in visited_nodes:
                continue
            elif node not in tentative_visits:
                tentative_visits[node] = dist_to_start + 1
            elif tentative_visits[node] > dist_to_start + 1:
                tentative_visits[node] = dist_to_start + 1

        tentative_visits.pop(current_node)
        visited_nodes[current_node] = dist_to_start

if __name__ == '__main__':
    node_grid, start_node, possible_starts = ingest_data_pt1()

    # give up on efficiency...
    min_dist = find_path_to_end(start_node)
    for node in possible_starts:
        dist = find_path_to_end(node)

        min_dist = min(dist, min_dist)

    print(min_dist)
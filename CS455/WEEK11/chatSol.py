class Solution:
    def hasPath(self, maze, start, destination):
        # create a stack for DFS
        stack = [start]

        # directions for up, down, left, right
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        # visited set to keep track of already visited nodes
        visited = set()

        # loop till stack is empty
        while stack:
            # pop a node from stack
            node = stack.pop()
            # mark the node as visited
            visited.add(node)
            # if this node is the destination, return True
            if node == tuple(destination):
                return True
            # check all four directions
            for dir in dirs:
                x, y = node
                # keep moving in current direction until hit the wall
                while 0 <= x + dir[0] < len(maze) and 0 <= y + dir[1] < len(maze[0]) and maze[x + dir[0]][y + dir[1]] == 0:
                    x += dir[0]
                    y += dir[1]
                # only add valid and non visited node to stack
                if (x, y) not in visited:
                    stack.append((x, y))

        return False


# Testing
maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [
    0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
start = (4, 3)
destination = (0, 1)

s = Solution()
print(s.hasPath(maze, start, destination))  # should return True

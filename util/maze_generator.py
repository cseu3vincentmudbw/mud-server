from django.contrib.auth.models import User
from adventure.models import Player, Room
import random
from util.constants import ROOM_NAMES, ROOM_DESCRIPTIONS

ALL_ROOMS = list(reversed(list(zip(ROOM_NAMES, ROOM_DESCRIPTIONS))))

CURRENT_ROOM = None

Room.objects.all().delete()

class Maze:
    """A Maze, represented as a grid of rooms."""

    def __init__(self, nx, ny, ix=0, iy=0):
        """Initialize the maze grid.
        The maze consists of nx x ny rooms and will be constructed starting
        at the room indexed at (ix, iy).

        """

        self.nx, self.ny = nx, ny
        self.ix, self.iy = ix, iy
        self.maze_map = [
            [Room.create(x, y) for y in range(ny)] for x in range(nx)
        ]

        for row in self.maze_map:
            for room in row:
                r_info = ALL_ROOMS.pop(0)
                room.title = r_info[0]
                room.description = r_info[1]
                room.save()


    def room_at(self, x, y):
        """Return the Room object at (x,y)."""

        return self.maze_map[x][y]

    def __str__(self):
        """Return a (crude) string representation of the maze."""

        maze_rows = ['-' * nx*2]
        for y in range(ny):
            maze_row = ['|']
            for x in range(nx):
                if self.maze_map[x][y].walls['E']:
                    maze_row.append(' |')
                else:
                    maze_row.append('  ')
            maze_rows.append(''.join(maze_row))
            maze_row = ['|']
            for x in range(nx):
                if self.maze_map[x][y].walls['S']:
                    maze_row.append('-+')
                else:
                    maze_row.append(' +')
            maze_rows.append(''.join(maze_row))
        return '\n'.join(maze_rows)

    def find_valid_neighbours(self, room):
        """Return a list of unvisited neighbours to room."""

        delta = [('W', (-1,0)),
                 ('E', (1,0)),
                 ('S', (0,1)),
                 ('N', (0,-1))]
        neighbours = []
        for direction, (dx,dy) in delta:
            x2, y2 = room.x + dx, room.y + dy
            if (0 <= x2 < nx) and (0 <= y2 < ny):
                neighbour = maze.room_at(x2, y2)
                if neighbour.has_all_walls():
                    neighbours.append((direction, neighbour))
        return neighbours

    def find_room_neighbours(self, room):
        """Return a list of all neighbours to room."""

        delta = [('W', (-1,0)),
                 ('E', (1,0)),
                 ('S', (0,1)),
                 ('N', (0,-1))]

        # Get all neighbours, including those separated by walls
        neighbours = []
        for direction, (dx,dy) in delta:
            x2, y2 = room.x + dx, room.y + dy
            if (0 <= x2 < nx) and (0 <= y2 < ny):
                neighbour = maze.room_at(x2, y2)
                neighbours.append((direction, neighbour))

        # Get all directions where the room has direct access to its
        # neighbours and is not separated by walls
        room_neighbours = []
        for direction, is_wall_present in room.walls.items():
            if not is_wall_present:
                room_neighbours.append(direction)
        return {direction:room for direction, room in neighbours if direction in room_neighbours }


    def make_maze(self):
        # Total number of rooms.
        n = self.nx * self.ny
        room_stack = []
        current_room = self.room_at(ix, iy)

        # Total number of visited rooms during maze construction.
        nv = 1

        while nv < n:
            neighbours = self.find_valid_neighbours(current_room)
            if not neighbours:
                # We've reached a dead end: backtrack.
                current_room = room_stack.pop()
                continue

            # Choose a random neighbouring room and move to it.
            direction, next_room = random.choice(neighbours)
            current_room.knock_down_wall(next_room, direction)
            room_stack.append(current_room)
            current_room = next_room
            nv += 1

# Maze dimensions (ncols, nrows)
nx, ny = 10, 10
# Maze entry position
ix, iy = 0, 0

maze = Maze(nx, ny, ix, iy)
maze.make_maze()

CURRENT_ROOM = maze.maze_map[ix][iy]

# # Make room connections
all_rooms = maze.maze_map
for row in all_rooms:
    for room in row:
        neighbours = maze.find_room_neighbours(room)
        if neighbours:
            for direction, neighbour in neighbours.items():
                room.connectRooms(neighbour, direction)

print(maze)


# Initialize players positions
players=Player.objects.all()
for p in players:
  p.currentRoom=CURRENT_ROOM.id
  p.save()

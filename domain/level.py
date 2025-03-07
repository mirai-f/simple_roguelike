from dataclasses import dataclass, field
from typing import List, Optional, Set, Dict, Tuple
from random import randint, sample
from numpy.random import choice
from .direction import Directions
from .point import Point
from .room import Room
from .corridor import Corridor
from .door import Door

from icecream import ic  # type: ignore


class Level:
    def __init__(self, level_number: int = 1):
        self.rooms: List[List[Room]] = []
        self.corridors: List[Corridor] = []
        self.level_number: int = level_number

        self.NUM_ROOMS_V: int = 3
        self.NUM_ROOMS_H: int = 3

        self.MINIMAL_DISTANCE_BETWEEN_ROOMS: int = 1
        self.HEIGHT: int = (
            self.NUM_ROOMS_V * Room.MAX_WIDTH
            + self.MINIMAL_DISTANCE_BETWEEN_ROOMS * (self.NUM_ROOMS_V + 1)
        )
        self.WIDTH: int = (
            self.NUM_ROOMS_H * Room.MAX_HEIGHT
            + self.MINIMAL_DISTANCE_BETWEEN_ROOMS * (self.NUM_ROOMS_H + 1)
        )

    def generate_level(self) -> None:
        self.generate_rooms()
        self.full_connect_rooms()
        self.generate_doors_and_corridors()

    def generate_rooms(self) -> None:
        self.rooms = [
            [Room((i, j)) for j in range(self.NUM_ROOMS_H)]
            for i in range(self.NUM_ROOMS_V)
        ]

    def full_connect_rooms(self) -> None:
        attempt: int = 0
        self.connect_rooms_random()
        while not self.is_level_fully_connected():
            if attempt > 100:
                raise RuntimeError(
                    "Не удалось создать полноценное соединение после 100 попыток."
                )
            self.connect_rooms_random()
            attempt += 1

    def connect_rooms_random(self) -> None:
        probabilities: list[float] = [7 / 12, 2 / 12, 2 / 12, 1 / 12]
        possible_count: list[int] = list(range(1, len(Directions.get_directions()) + 1))

        for i in range(self.NUM_ROOMS_V):
            for j in range(self.NUM_ROOMS_H):
                options: List[str] = list(Directions.get_directions().keys())
                random_count: int = choice(possible_count, p=probabilities)
                random_subset: List[str] = sample(options, random_count)

                for option in random_subset:
                    di, dj = Directions.get_direction(option)
                    ni, nj = i + di, j + dj

                    if 0 <= ni < self.NUM_ROOMS_V and 0 <= nj < self.NUM_ROOMS_H:
                        room_a = self.rooms[i][j]
                        room_b = self.rooms[ni][nj]

                        room_a.connected_rooms.add(room_b)
                        room_b.connected_rooms.add(room_a)

    def is_level_fully_connected(self) -> bool:
        all_rooms = [room for row in self.rooms for room in row]

        visited = set()
        stack = [all_rooms[0]]

        while stack:
            current_room = stack.pop()
            visited.add(current_room)

            for connected_room in current_room.connected_rooms:
                if connected_room not in visited:
                    stack.append(connected_room)

        return len(visited) == len(all_rooms)

    def is_rooms_connect(self, room_a: Room, room_b: Room):
        return room_a in room_b.connected_rooms

    def generate_doors_proc(self, direct: str, room_out: Room, room_in: Room):
        height_out, width_out = room_out.HEIGHT, room_out.WIDTH
        height_in, width_in = room_in.HEIGHT, room_in.WIDTH
        l_c_room_out = room_out.l_c
        l_c_room_in = room_in.l_c

        coordinates_out: Dict[str, Point] = {
            "up": Point(0, randint(1, width_out - 2)) + l_c_room_out,
            "down": Point(height_out - 1, randint(1, width_out - 2)) + l_c_room_out,
            "left": Point(randint(1, height_out - 2), 0) + l_c_room_out,
            "right": Point(randint(1, height_out - 2), width_out - 1) + l_c_room_out,
        }
        coordinates_in: Dict[str, Point] = {
            "up": Point(height_in - 1, randint(1, width_in - 2)) + l_c_room_in,
            "down": Point(0, randint(1, width_in - 2)) + l_c_room_in,
            "left": Point(randint(1, height_in - 2), width_in - 1) + l_c_room_in,
            "right": Point(randint(1, height_in - 2), 0) + l_c_room_in,
        }

        room_out.doors.append(Door(direct, l_c=coordinates_out[direct]))
        room_in.doors.append(
            Door(Directions.get_opposite_direction(direct), l_c=coordinates_in[direct])
        )

    def generate_corridors_proc(self, direct: str, room_out: Room, room_in: Room):
        g_c_cell_room_out = room_out.get_g_c_cell(self.MINIMAL_DISTANCE_BETWEEN_ROOMS)
        g_c_cell_room_in = room_in.get_g_c_cell(self.MINIMAL_DISTANCE_BETWEEN_ROOMS)

        g_c_door_out = g_c_cell_room_out + room_out.doors[-1].l_c
        g_c_door_in = g_c_cell_room_in + room_in.doors[-1].l_c

        corridor = Corridor((room_out.ID, room_in.ID))
        corridor.generate_path(direct, g_c_door_out, g_c_door_in)
        self.corridors.append(corridor)

    def generate_doors_and_corridors(self):
        connections = set()
        for i in range(self.NUM_ROOMS_V):
            for j in range(self.NUM_ROOMS_H):
                for direct, (di, dj) in Directions.get_directions().items():
                    ni, nj = i + di, j + dj

                    if not (0 <= ni < self.NUM_ROOMS_V and 0 <= nj < self.NUM_ROOMS_H):
                        continue

                    room_out = self.rooms[i][j]
                    room_in = self.rooms[ni][nj]

                    connection = frozenset([room_out.ID, room_in.ID])
                    if connection in connections:
                        continue

                    if self.is_rooms_connect(room_out, room_in):
                        self.generate_doors_proc(direct, room_out, room_in)
                        self.generate_corridors_proc(direct, room_out, room_in)
                        connections.add(connection)

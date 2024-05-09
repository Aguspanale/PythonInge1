import pytest
from Mars_Rover import Mars_Rover
from Cardinal import *

class Test_Mars_Rover:

    def setup_method(self):
        self.default_position = (0, 0)
        self.default_north_direction = North()
        self.default_north_facing_mars_rover = Mars_Rover(self.default_position, self.default_north_direction)
        self.default_south_direction = South()
        self.default_south_facing_mars_rover = Mars_Rover(self.default_position, self.default_south_direction)

    def test_01_mars_rover_starts_where_it_should(self):
        assert self.default_north_facing_mars_rover.position == self.default_position, 'mars rover not in correct position!'
        assert self.default_north_facing_mars_rover.direction == self.default_north_direction

    def test_02_mars_rover_moves_forward(self):
        self.default_north_facing_mars_rover.receive('f')
        assert self.default_north_facing_mars_rover.position == (0, 1)

    def test_03_mars_rover_moves_forward_twice(self):
        self.default_north_facing_mars_rover.receive('f')
        self.default_north_facing_mars_rover.receive('f')
        assert self.default_north_facing_mars_rover.position == (0, 2)

    def test_04_mars_rover_moves_forward_facing_south(self):
        self.default_south_facing_mars_rover.receive('f')
        assert self.default_south_facing_mars_rover.position == (0, -1)

    def test_05_mars_rover_moves_forward_with_composed_message(self):
        self.default_north_facing_mars_rover.receive('ff')
        assert self.default_north_facing_mars_rover.position == (0, 2)

    def test_06_mars_rover_moves_backwards(self):
        self.default_north_facing_mars_rover.receive('b')
        assert self.default_north_facing_mars_rover.position == (0, -1)

    def test_07_mars_rover_move_backward_and_forward_to_starting_position(self):
        self.default_north_facing_mars_rover.receive('bffb')
        assert self.default_north_facing_mars_rover.position == (0, 0)

    def test_08_mars_rover_rotates_right(self):
        self.default_north_facing_mars_rover.receive('r')
        assert self.default_north_facing_mars_rover.direction.isEast()

    def test_09_mars_rover_rotates_right_twice(self):
        self.default_north_facing_mars_rover.receive('rr')
        assert self.default_north_facing_mars_rover.direction.isSouth()
    def test_10_mars_rover_rotates_left(self):
        self.default_north_facing_mars_rover.receive('l')
        assert self.default_north_facing_mars_rover.direction.isWest()
    def test_11_mars_rover_rotates_left_twice(self):
        self.default_north_facing_mars_rover.receive('ll')
        assert self.default_north_facing_mars_rover.direction.isSouth()
    def test_12_mars_rover_ignores_unknown_instruction(self):
        self.default_north_facing_mars_rover.receive('asd')
        assert self.default_north_facing_mars_rover.position == (0, 0) and self.default_north_facing_mars_rover.direction.isNorth()
    def test_13_mars_rover_stops_receiving_message_after_unknown_instruction(self):
        self.default_north_facing_mars_rover.receive('llprr')
        assert self.default_north_facing_mars_rover.position == (0, 0) and self.default_north_facing_mars_rover.direction.isSouth()



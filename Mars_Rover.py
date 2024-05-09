from Cardinal import *
class Mars_Rover:

    def __init__(self,position,direction):
        self.position = position
        self.direction = direction
        self._instructions = {
            'f': lambda: self.move_forwards(),
            'b': lambda: self.move_backwards(),
            'r': lambda: self.rotate_right(),
            'l': lambda: self.rotate_left()
        }

    def receive(self,message):
        for instruction in message:
            if instruction in self._instructions:
                self._instructions.get(instruction)()
            else:
                break

    def rotate_left(self):
        self.direction = self.direction.rotate_left()

    def rotate_right(self):
        self.direction = self.direction.rotate_right()

    def move_backwards(self):
        self.position = tuple(x - y for x, y in zip(self.position, self.direction.unit_vector()))

    def move_forwards(self):
        self.position = tuple(x + y for x, y in zip(self.position, self.direction.unit_vector()))

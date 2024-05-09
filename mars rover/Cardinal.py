from abc import abstractmethod,ABCMeta


class Cardinal(metaclass=ABCMeta):
    @abstractmethod
    def unit_vector(self):
        pass

    @abstractmethod
    def rotate_right(self):
        pass
    @abstractmethod
    def rotate_left(self):
        pass
    def isNorth(self):
        return False
    def isSouth(self):
        return False
    def isEast(self):
        return False
    def isWest(self):
        return False


class North(Cardinal):
    def unit_vector(self):
        return (0,1)
    def rotate_right(self):
        return East()
    def rotate_left(self):
        return West()
    def isNorth(self):
        return True


class South(Cardinal):
    def unit_vector(self):
        return (0,-1)

    def rotate_right(self):
        return West()
    def rotate_left(self):
        return East()
    def isSouth(self):
        return True


class East(Cardinal):
    def unit_vector(self):
        return (1,0)

    def rotate_right(self):
        return South()
    def rotate_left(self):
        return North()

    def isEast(self):
        return True


class West(Cardinal):
    def unit_vector(self):
        return (-1,0)
    def rotate_right(self):
        return North()
    def rotate_left(self):
        return South()
    def isWest(self):
        return True

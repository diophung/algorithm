class Asteroid(object):
    """
    Given list of asteroid, find how many will hit the station

    Asteroid: (mass, direction), direction: 1 = incoming, -1 = not incoming.
    All asteroids move at same speed.
    If 2 asteroids clash, the bigger one destroy the other completely.
    """

    def __init__(self, mass, direction):
        self.mass = mass
        self.direction = direction

    def __str__(self):
        return 'Asteroid({},{})'.format(self.mass, self.direction)


class AsteroidsCount:

    @staticmethod
    def count(asteroids):
        survivor = asteroids[-1]
        right_to_left = asteroids[:-1][::-1]  # reverse list, without last asteroid
        c = 0 if survivor.direction == -1 else 1
        for el in right_to_left:
            if el.direction != survivor:
                survivor = el if el.mass > survivor.mass else survivor
            else:
                survivor = el
            if survivor.direction == 1:
                c += 1
        return c

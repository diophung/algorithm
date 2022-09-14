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
    """
    Given a space station and a list of asteroids with masses and moving direcitions.
    Two asteroids going in different direction will cancel each other and create a new 
    asteroid, with the new mass equals to the difference between the two, and the direction
    is following the larger asteroid.
    
    The goal is to find out if the space station will be hit by any asteroid.

                         Asteroid1              Asteroid2                  AsteroidN
    [SPACE STATION]      (mass=7, dir=AWAY)      (mass=2, DIR=COMING)     (mass=3, dir=COMING)
    
    The goal is to know what is the final number of asteroid and their direction    
    """

    @staticmethod
    def count(asteroids):
        """
        Args:
            asteroids: list of integers, the sign is the direction, 
                       (-) for going away, (+) is coming into and velocity of each
    
        """
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

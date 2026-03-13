import random

class particle:
    def __init__(self, limits:list[tuple[float, float]]):
        self.limits = limits
        self.dim = len(limits)

        #self.position = # todo 
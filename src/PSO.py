import utils as u
from particle import particle

class PSO:
    def __init__(self, n_particles:int, limits:list[tuple[float, float]], w:float, c1:float, c2:float, max_iter:int):
        self.limits = limits
        self.dim = len(limits)
        self.particles = [particle(limits) for _ in range(n_particles)]
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.max_iter = max_iter
        self.gbest_position = None
        self.gbest_fitness = float('inf')
        
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
    
    def initialize_swarm(self, fitness_func):
        """Metodo para inicializar el enjambre"""
        for particle in self.particles:
            particle.evaluate(fitness_func)
            if particle.best_fitness < self.gbest_fitness:
                self.gbest_fitness = particle.best_fitness
                self.gbest_position = particle.best_position.copy()
    
        
    def optimize(self, fitness_func):
        """Metodo para ejecutar el algoritmo principal PSO"""
        self.initialize_swarm(fitness_func)
        for i in range(self.max_iter):
            for particle in self.particles:
                particle.update_velocity(self.w, self.c1, self.c2, self.gbest_position)
                particle.update_position()
                particle.evaluate(fitness_func)
                if particle.best_fitness < self.gbest_fitness:
                    self.gbest_fitness = particle.best_fitness
                    self.gbest_position = particle.best_position.copy()
        return self.gbest_position, self.gbest_fitness
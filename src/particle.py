import random

class particle:
    def __init__(self, limits:list[tuple[float, float]]):
        self.limits = limits
        self.dim = len(limits)
        self.position = [random.uniform(min_i, max_i) for (min_i, max_i) in limits]
        self.velocity = [random.uniform(-1,1) for _ in range(self.dim)]
        
        self.best_position = self.position.copy()
        self.best_fitness = float('inf')

    def evaluate(self, fitness_func):
        current_fitness = fitness_func(self.position)
        if current_fitness < self.best_fitness:
            self.best_fitness = current_fitness
            self.best_position = self.position
        return current_fitness
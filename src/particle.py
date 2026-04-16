import random

class particle:
    def __init__(self, limits:list[tuple[float, float]]):
        self.limits = limits
        self.dim = len(limits)
        self.position = [random.uniform(min_i, max_i) for (min_i, max_i) in limits]
        # Iniciar la velocidad proporcional al tamaño del espacio de búsqueda (ej. 10%)
        self.velocity = [random.uniform(-0.1 * (max_i - min_i), 0.1 * (max_i - min_i)) for (min_i, max_i) in limits]
        
        self.best_position = self.position.copy()
        self.best_fitness = float('inf')

    def evaluate(self, fitness_func):
        """Metodo para evaluar el fitness de la particula"""
        current_fitness = fitness_func(self.position)
        if current_fitness < self.best_fitness:
            self.best_fitness = current_fitness
            self.best_position = self.position.copy()
        return current_fitness

    def update_velocity(self, w:float, c1:float, c2:float, gbest_position:list[float]):
        """Metodo para actualizar la velocidad de la particula"""
        new_velocity = []
        for i in range(self.dim):
            r1 = random.uniform(0,1)
            r2 = random.uniform(0,1)
            cognitive_component = c1 * r1 * (self.best_position[i] - self.position[i])
            social_component = c2 * r2 * (gbest_position[i] - self.position[i])
            new_velocity.append(w * self.velocity[i] + cognitive_component + social_component)
        self.velocity = new_velocity

    def update_position(self):
        """Metodo para actualizar la posicion de la particula"""
        new_position = []
        for i in range(self.dim):
            calculated_position = self.position[i] + self.velocity[i]
            if calculated_position < self.limits[i][0]:
                calculated_position = self.limits[i][0]
                self.velocity[i] = 0.0 # Resetear velocidad si choca con el límite
            elif calculated_position > self.limits[i][1]:
                calculated_position = self.limits[i][1]
                self.velocity[i] = 0.0 # Resetear velocidad si choca con el límite
            new_position.append(calculated_position)
        self.position = new_position

    
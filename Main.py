from src.PSO import PSO

# Función objetivo (esfera)
target_func = lambda x: x[0]**2 + x[1]**2


if __name__ == "__main__":
    # Parámetros del PSO
    n_particles = 30
    limits = [(-10, 10), (-10, 10)]  # Límites de las variables
    w = 0.7
    c1 = 1.5
    c2 = 1.5
    max_iter = 100

    # Crear y ejecutar el PSO
    pso = PSO(n_particles, limits, w, c1, c2, max_iter)
    best_position, best_fitness = pso.optimize(target_func)

    print("Mejor posición encontrada:", best_position)
    print("Mejor fitness encontrado:", best_fitness)
import math
import random
import matplotlib.pyplot as plt


# 定义适应函数
def fitness_function(x, y, z, k):
    # 2911	160	37	7.0
    return math.sqrt((x - 4364 / 4000) ** 2 + (y - 153 / 120) ** 2 + (z - 207 / 200) ** 2 + (k - 7 / 7) ** 2)


# 初始化粒子群
class Particle:
    def __init__(self, x_bounds, y_bounds, z_bounds, k_bounds):
        self.position = [random.uniform(x_bounds[0], x_bounds[1]),
                         random.uniform(y_bounds[0], y_bounds[1]),
                         random.uniform(z_bounds[0], z_bounds[1]),
                         random.uniform(k_bounds[0], k_bounds[1])]
        self.velocity = [0, 0, 0]
        self.best_position = self.position[:]
        self.best_fitness = fitness_function(*self.position)


class Swarm:
    def __init__(self, n_particles, x_bounds, y_bounds, z_bounds, k_bounds):
        self.particles = [Particle(x_bounds, y_bounds, z_bounds, k_bounds) for _ in range(n_particles)]
        self.global_best_position = self.particles[0].position[:]
        self.global_best_fitness = fitness_function(*self.global_best_position)

    # 粒子群优化算法主循环
    def optimize(self, n_iterations, w, c1, c2):
        global_best_position_trace = []
        global_best_fitness_trace = []
        for iteration in range(n_iterations):
            for particle in self.particles:
                # 更新速度
                for i in range(3):
                    r1 = random.uniform(0, 1)
                    r2 = random.uniform(0, 1)
                    particle.velocity[i] = w * particle.velocity[i] + c1 * r1 * (
                            particle.best_position[i] - particle.position[i]) + c2 * r2 * (
                                                   self.global_best_position[i] - particle.position[i])
                # 更新位置
                for i in range(3):
                    particle.position[i] += particle.velocity[i]
                # 更新个体最优
                fitness = fitness_function(*particle.position)
                if fitness < particle.best_fitness:
                    particle.best_fitness = fitness
                    particle.best_position = particle.position[:]
                # 更新全局最优
                if fitness < self.global_best_fitness:
                    self.global_best_fitness = fitness
                    self.global_best_position = particle.position[:]
            global_best_position_trace.append(self.global_best_position)
            global_best_fitness_trace.append(self.global_best_fitness)
            # print(f"Iteration {iteration + 1}: global best position = {self.global_best_position},"
            #       f" global best fitness = {self.global_best_fitness}")
        # 绘制收敛曲线
        K_Temperature = []
        Nits = []
        Glare_index = []
        Sleep_time = []
        for position in global_best_position_trace:
            K_Temperature.append(position[0])
            Nits.append(position[1])
            Glare_index.append(position[2])
            Sleep_time.append(position[3])
        # print(K_Temperature)
        # print(Nits)
        # print(Glare_index)
        # print(Sleep_time)
        plt.plot(K_Temperature, label="Color temperature/ 4000(K)")
        plt.plot(Nits, label="Artificial light intensity/ 120(nits)")
        plt.plot(Glare_index, label="Glare index/35 (μcd/m²)")
        plt.plot(Sleep_time, label="Average sleep Time/7 (h/day)")
        plt.xlabel('Iteration')
        plt.ylabel('Fitness Function Value of Each Interation')
        plt.legend(loc='lower right')
        plt.show()


# 运行粒子群算法
N_range = [0, 1.5]
swarm = Swarm(n_particles=100, x_bounds=N_range, y_bounds=N_range, z_bounds=N_range, k_bounds=N_range)
swarm.optimize(n_iterations=100, w=0.8, c1=1.5, c2=1.5)

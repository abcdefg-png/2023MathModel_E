import math
import random
import matplotlib.pyplot as plt


# 定义适应函数
def fitness_function(y, z):
    return math.sqrt((y - 1.63) ** 2 + (z - 0.98) ** 2)


# 初始化粒子群
class Particle:
    def __init__(self, y_bounds, z_bounds):
        self.position = [random.uniform(y_bounds[0], y_bounds[1]),
                         random.uniform(z_bounds[0], z_bounds[1])]
        self.velocity = [0, 0, 0]
        self.best_position = self.position[:]
        self.best_fitness = fitness_function(*self.position)


class Swarm:
    def __init__(self, n_particles, y_bounds, z_bounds):
        self.particles = [Particle(y_bounds, z_bounds) for _ in range(n_particles)]
        self.global_best_position = self.particles[0].position[:]
        self.global_best_fitness = fitness_function(*self.global_best_position)

    # 粒子群优化算法主循环
    def optimize(self, n_iterations, w, c1, c2):
        global_best_position_trace = []
        global_best_fitness_trace = []
        for iteration in range(n_iterations):
            for particle in self.particles:
                # 更新速度
                for i in range(2):
                    r1 = random.uniform(0, 1)
                    r2 = random.uniform(0, 1)
                    particle.velocity[i] = w * particle.velocity[i] + c1 * r1 * (
                            particle.best_position[i] - particle.position[i]) + c2 * r2 * (
                                                   self.global_best_position[i] - particle.position[i])
                # 更新位置
                for i in range(2):
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
            print(f"Iteration {iteration + 1}: global best position = {self.global_best_position},"
                  f" global best fitness = {self.global_best_fitness}")
        # 绘制收敛曲线
        Brightness = []
        angle = []
        for position in global_best_position_trace:
            Brightness.append(position[0])
            angle.append(position[1])
        plt.plot(Brightness, label="I/100(nits)")
        plt.plot(angle, label="θ(°)")
        plt.xlabel('Iteration')
        plt.ylabel('Best Particle of Each Interation')
        plt.legend(loc='lower right')
        plt.show()


# 运行粒子群算法
swarm = Swarm(n_particles=300, y_bounds=[50, 300], z_bounds=[0, 1.57])
swarm.optimize(n_iterations=100, w=0.8, c1=1.5, c2=1.5)

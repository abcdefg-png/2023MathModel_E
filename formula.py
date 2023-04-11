import math
import numpy as np


# def fun1(x0, x1, x2):
#     return 10 * math.sqrt(x0) * math.pow(x1, 0.8) * math.cos(2 * x2)
#
#
# def fun2(x0, x1, x2):
#     return 15.2 + 0.62 * x0 - 0.47 * x1 + 5.8 * np.cos(x2) + 16.4
#
#
# def fun3(x0, x1, x2):
#     return 4000 * math.cos(x2) * x0 ** 0.4 * x1 ** 0.7 + 5500 * (1 - math.cos(x2)) + 0.1
#
#
# def fun4(x0, x1, x2):
#     return 0.034 * x0 ** 0.7 * x1 ** 0.63 * np.cos(1.3 * x2)


def normalize(func_values):
    means = [np.mean(values) for values in func_values]
    stds = [np.std(values) for values in func_values]
    normalized_values = []
    for i in range(len(func_values)):
        values = func_values[i]
        mean = means[i]
        std = stds[i]
        normalized_values.append([(value - mean) / std for value in values])
    return normalized_values


def fitness_function1(x):  # 适应函数
    fun1 = 100 * math.sqrt(x[0]) * math.pow(x[1], 0.8) * math.cos(2 * x[2])
    fun2 = 15.2 + 0.62 * x[0] - 0.27 * x[1] + 5.8 * np.cos(x[2]) + 16.4
    fun3 = 2000 * math.cos(x[2]) * x[0] ** 0.4 * x[1] ** 0.7 + 2500 * (1 - math.cos(x[2])) + 0.1
    fun4 = 0.034 * x[0] ** 0.7 * x[1] ** 0.63 * np.cos(1.3 * x[2])
    fun5 = 6 + 0.1 * x[0] + 0.05 * x[1] + 0.02 * math.cos(2 * x[2])
    w1, w2, w3, w4, w5 = 1.20, 0.18, 0.18, 0.18, 0.18
    fun1_norm = (fun1 - np.min([fun1, fun2, fun3, fun4, fun5])) / (
            np.max([fun1, fun2, fun3, fun4, fun5]) - np.min([fun1, fun2, fun3, fun4, fun5]))
    fun2_norm = (fun2 - np.min([fun1, fun2, fun3, fun4, fun5])) / (
            np.max([fun1, fun2, fun3, fun4, fun5]) - np.min([fun1, fun2, fun3, fun4, fun5]))
    fun3_norm = (fun3 - np.min([fun1, fun2, fun3, fun4, fun5])) / (
            np.max([fun1, fun2, fun3, fun4, fun5]) - np.min([fun1, fun2, fun3, fun4, fun5]))
    fun4_norm = (fun4 - np.min([fun1, fun2, fun3, fun4, fun5])) / (
            np.max([fun1, fun2, fun3, fun4, fun5]) - np.min([fun1, fun2, fun3, fun4, fun5]))
    fun5_norm = (fun5 - np.min([fun1, fun2, fun3, fun4, fun5])) / (
            np.max([fun1, fun2, fun3, fun4, fun5]) - np.min([fun1, fun2, fun3, fun4, fun5]))
    funres = w1 * fun1_norm + w2 * fun2_norm + w3 * fun3_norm + w4 * fun4_norm - w5 * fun5_norm
    return funres.round(8)

    # fun1 = 10 * math.sqrt(x[0]) * math.pow(x[1], 0.8) * math.cos(2 * x[2])
    # fun2 = 15.2 + 0.62 * x[0] - 0.47 * x[1] + 5.8 * np.cos(x[2]) + 16.4
    # fun3 = 4000 * math.cos(x[2]) * x[0] ** 0.4 * x[1] ** 0.7 + 5500 * (1 - math.cos(x[2])) + 0.1
    # fun4 = 0.034 * x[0] ** 0.7 * x[1] ** 0.63 * np.cos(1.3 * x[2])
    # fun5 = 6 + 0.1 * x[0] - 0.05 * x[1] - 0.02 * math.cos(2 * x[2])
    # print(fun1 * 10, fun2 * 100, fun3 / 40, fun4, fun5 * 3)
    # x[2] = np.rad2deg(np.arccos(x[2]))


# Example usage
x = [10, 22, 1]  # function input values
fun1 = [10 * math.sqrt(x[0]) * math.pow(x[1], 0.8) * math.cos(2 * x[2])]
fun2 = [15.2 + 0.62 * x[0] - 0.47 * x[1] + 5.8 * np.cos(x[2]) + 16.4]
fun3 = [4000 * math.cos(x[2]) * x[0] ** 0.4 * x[1] ** 0.7 + 5500 * (1 - math.cos(x[2])) + 0.1]
fun4 = [0.034 * x[0] ** 0.7 * x[1] ** 0.63 * np.cos(1.3 * x[2])]

# Normalize function values
print(np.deg2rad(90))

"""
Logistic映射与混沌系统研究
"""

import numpy as np
import matplotlib.pyplot as plt

def iterate_logistic(r, x0, n):
    """
    迭代Logistic映射
    
    参数:
        r: 增长率参数
        x0: 初始值
        n: 迭代次数
        
    返回:
        x: 迭代序列数组
    """
    pass

def plot_time_series(r, x0, n):
    """
    绘制时间序列图
    
    参数:
        r: 增长率参数
        x0: 初始值
        n: 迭代次数
        
    返回:
        fig: matplotlib图像对象
    """
    pass

def plot_bifurcation(r_min, r_max, n_r, n_iterations, n_discard):
    """
    绘制分岔图
    
    参数:
        r_min: r的最小值
        r_max: r的最大值
        n_r: r的取值个数
        n_iterations: 每个r值的迭代次数
        n_discard: 每个r值丢弃的初始迭代点数
        
    返回:
        fig: matplotlib图像对象
    """
    pass

def main():
    """主函数"""
    # 时间序列分析
    r_values = [2.0, 3.2, 3.45, 3.6]
    x0 = 0.5
    n = 100
    
    for r in r_values:
        fig = plot_time_series(r, x0, n)
        fig.savefig(f"logistic_r{r}.png", dpi=300)
        plt.close(fig)
    
    # 分岔图分析
    fig = plot_bifurcation(2.5, 4.0, 1000, 1000, 100)
    fig.savefig("bifurcation.png", dpi=300)
    plt.close(fig)

if __name__ == "__main__":
    main()

    import numpy as np
import matplotlib.pyplot as plt


# Logistic 模型迭代函数
def logistic_iteration(r, x0, n):
    x = np.zeros(n)
    x[0] = x0
    for i in range(1, n):
        x[i] = r * x[i - 1] * (1 - x[i - 1])
    return x


# 任务 1：Logistic 模型的迭代
def task1():
    r_values = [2, 3.2, 3.45, 3.6]
    x0 = 0.5
    n_iterations = 60

    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes = axes.flatten()

    for i, r in enumerate(r_values):
        x = logistic_iteration(r, x0, n_iterations)
        axes[i].plot(range(n_iterations), x)
        axes[i].set_title(f'r = {r}')
        axes[i].set_xlabel('迭代次数')
        axes[i].set_ylabel('x')

        if r == 2:
            print(f"当 r = {r} 时，x 趋于 0.5，结论为没有分岔。")
        elif r == 3.2:
            print(f"当 r = {r} 时，x 趋于两个值，结论为周期 2 分岔。")
        elif r == 3.45:
            print(f"当 r = {r} 时，x 趋于四个值，结论为周期 4 分岔。")
        elif r == 3.6:
            print(f"当 r = {r} 时，x 的取值没有明确趋向，结论为混沌。")

    plt.tight_layout()
    plt.show()


# 任务 2：费根鲍姆图的绘制
def task2():
    r_min = 2.6
    r_max = 4
    r_step = 0.001
    r_values = np.arange(r_min, r_max, r_step)
    x0 = 0.5
    n_iterations = 250
    n_discard = 100

    x_values = []
    for r in r_values:
        x = logistic_iteration(r, x0, n_iterations)
        x_values.append(x[n_discard:])

    plt.figure(figsize=(10, 6))
    for i, r in enumerate(r_values):
        plt.scatter([r] * len(x_values[i]), x_values[i], s=0.1, color='k')

    plt.title('费根鲍姆图')
    plt.xlabel('r')
    plt.ylabel('x')
    plt.show()


if __name__ == "__main__":
    task1()
    task2()
    
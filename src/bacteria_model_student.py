import numpy as np
import matplotlib.pyplot as plt
#1.1 a
A=1
tau=1
t=np.linspace(0, 2, 100)
W=A*(np.exp(-t/tau) - 1 + t/tau)

plt.plot(t, W)
plt.xlabel('t')
plt.ylabel('W(t)')
plt.title('W(t) for A = 1, tau = 1')
plt.show()

#1.1 b
params = [(1, 1), (2, 1), (1, 2)]
for i, (tau, A) in enumerate(params):
    t = np.linspace(0, 2, 100)
    W = A * (np.exp(-t/tau) - 1 + t/tau)
    plt.plot(t, W, label=f'W{i+1}, A={A}, tau={tau}')
plt.xlabel('t')
plt.ylabel('W(t)')
plt.title('Multiple W(t) functions')
plt.legend()
plt.show()

#1.1 c
params = [(1, 1), (2, 1), (1, 2)]
styles = ['-r', '--g', '-.b']  #改变颜色
for i, ((tau, A), style) in enumerate(zip(params, styles)):
    t = np.linspace(0, 2, 100)
    W = A * (np.exp(-t/tau) - 1 + t/tau)
    plt.plot(t, W, style, label=f'W{i+1}, A={A}, tau={tau}')
plt.xlabel('t')
plt.ylabel('W(t)')
plt.title('Multiple W(t) functions with different styles')
plt.legend()
plt.show()

#1.1 d
params = [(1, 1), (2, 1), (1, 2)]
styles = ['-r', '--g', '-.b']
for i, ((tau, A), style) in enumerate(zip(params, styles)):
    t = np.linspace(0, 2, 100)
    W = A * (np.exp(-t/tau) - 1 + t/tau)
    plt.plot(t, W, style, label=f'W{i+1}, A={A}, tau={tau}')
plt.xlabel('t')
plt.ylabel('W(t)')
plt.title('Multiple W(t) functions with different styles')
plt.legend()
plt.grid(True)
plt.xlim(0, 2)
plt.ylim(bottom=0)
plt.show()

#1.2 a

with open('g149novickA.txt', 'r') as file:
    lines = file.readlines()
t_data = []
W_data = []
for line in lines:
    parts = line.strip().split()  # 按空格分割每行数据
    t_str = parts[0].rstrip(',')  # 去除时间数据末尾的逗号
    w_str = parts[1].rstrip(',')  # 去除W值数据末尾的逗号
    t_data.append(float(t_str))
    W_data.append(float(w_str))
# 将列表转换为numpy数组
t_data = np.array(t_data)
W_data = np.array(W_data)
# 绘制实验数据点
plt.scatter(t_data, W_data, marker='o', label='Experimental Data Points')
# 选择多组不同的A和tau值
param_sets = [(1, 2),(1, 1.5)]
for A, tau in param_sets:
    t = np.linspace(0, np.max(t_data), 100)
    W = A * (np.exp(-t / tau) - 1 + t / tau)
    plt.plot(t, W, label=f'W(t), A={A}, tau={tau}')
plt.xlabel('Time (t)')
plt.ylabel('W(t)')
plt.title('Combined Experimental Data and Theoretical Curves')
plt.legend()
plt.show()

#1.2 b
with open('g149novickB.txt', 'r') as file:
    lines = file.readlines()
t_data = []
W_data = []
for line in lines:
    parts = line.strip().split()  # 按空格分割每行数据
    t_str = parts[0].rstrip(',')  # 去除时间数据末尾的逗号
    w_str = parts[1].rstrip(',')  # 去除W值数据末尾的逗号
    t_data.append(float(t_str))
    W_data.append(float(w_str))
# 将列表转换为numpy数组
t_data = np.array(t_data)
W_data = np.array(W_data)
# 筛选时间小于十小时的数据
mask = t_data < 10
t_filtered = t_data[mask]
W_filtered = W_data[mask]

# 绘制筛选后的数据点
plt.scatter(t_filtered, W_filtered, label='Filtered Experimental Data')

# 绘制理论曲线并调整参数拟合
A = 1  # 假设初始值
tau = 1  # 假设初始值
t = np.linspace(0, np.max(t_filtered), 100)
W = A * (np.exp(-t / tau) - 1 + t / tau)
plt.plot(t, W, '-r', label=f'W(t), A={A}, tau={tau}')
plt.xlabel('t')
plt.ylabel('W(t)')
plt.title('Fitting Filtered Experimental Data')
plt.legend()
plt.show()

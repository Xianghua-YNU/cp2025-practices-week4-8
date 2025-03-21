import numpy as np
import matplotlib.pyplot as plt

class HIVModel:
    def __init__(self, A, alpha, B, beta):
        self.A = A
        self.alpha = alpha
        self.B = B
        self.beta = beta

    def viral_load(self, time):
        return self.A * np.exp(-self.alpha * time) + self.B * np.exp(-self.beta * time)

    def plot_model(self, time):
        viral_load = self.viral_load(time)
        plt.plot(time, viral_load, label='Model')
        plt.xlabel('Time (days)')
        plt.ylabel('Viral Load')
        plt.title('HIV Viral Load Model Fitting')
        plt.legend()
        plt.show()

def load_hiv_data(filepath):
    try:
        data = np.load(filepath)
        time_data = data['time_in_days']
        viral_load_data = data['viral_load']
        return time_data, viral_load_data
    except:
        data = np.loadtxt(filepath, delimiter=',')
        time_data = data[:, 0]
        viral_load_data = data[:, 1]
        return time_data, viral_load_data

def main():
    # 初始化模型参数
    model = HIVModel(A=1000, alpha=0.5, B=500, beta=0.1)
    
    # 生成时间序列
    time = np.linspace(0, 10, 100)
    
    # 计算并绘制模型曲线
    model.plot_model(time)
    
    # 加载实验数据
    time_data, viral_load_data = load_hiv_data('HIVseries.npz')
    
    # 绘制实验数据
    plt.scatter(time_data, viral_load_data, label='Experimental Data')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

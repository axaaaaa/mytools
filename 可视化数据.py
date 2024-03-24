

# 导入matplotlib库
import matplotlib.pyplot as plt

# 定义数据
area = ["石牌", "冷水", "莫愁湖", "双河", "丰乐"]
task_num = [442, 332, 111, 223, 124]
complete_num = [44, 332, 56, 123, 65]
complete_rate = [9.95, 100.00, 50.45, 55.16, 52.42]
missing_num = [12, 4, 5 ,0 ,1]


# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 设置柱状图的位置和宽度
bar_width = 0.2
x1 = list(range(len(area)))
x2 = [i + bar_width for i in x1]
x3 = [i + bar_width for i in x2]
x4 = [i + bar_width for i in x3]

# 绘制柱状图
plt.bar(x1, task_num, width=bar_width, color="blue", label="任务数")
plt.bar(x2, complete_num , width=bar_width,color="green", label="完成数")
plt.bar(x3 , complete_rate , width=bar_width,color="red", label="完成率")
plt.bar(x4 , missing_num , width=bar_width,color="orange", label="疑似失踪数")

# 设置横坐标标签
plt.xticks([i + bar_width for i in x1], area)

# 设置标题和轴标签
plt.title("各地区任务情况")
plt.xlabel("地区")
plt.ylabel("数量或百分比")

# 显示图例
plt.legend()

# 显示或保存图形
plt.show()
#plt.savefig("bar_chart.png")
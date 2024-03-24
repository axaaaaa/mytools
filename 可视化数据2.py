import matplotlib.pyplot as plt

# 数据
regions = ['石牌（联络员:1）', '冷水（联络员:2）', '莫愁湖（联络员:3）', '双河（联络员:4）', '丰乐（联络员:5）']
task_counts = [442, 332, 111, 223, 124]
completed_counts = [44, 332, 56, 123, 65]

completion_rates = [c / t * 100 for t, c in zip(task_counts, completed_counts)]

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建画布和子图
fig, ax1 = plt.subplots()

# 绘制柱状图
bar_width = 0.35
opacity = 0.8
index = range(len(regions))
rects1 = ax1.bar(index, task_counts, bar_width,
                alpha=opacity, color='b', label='任务数')
rects2 = ax1.bar([i + bar_width for i in index], completed_counts, bar_width,
                alpha=opacity, color='r', label='完成数')


# 设置第一个坐标轴属性
ax1.set_xlabel('地区')
ax1.set_ylabel('数量')
ax1.set_title('任务数与完成数')
ax1.set_xticks([i + bar_width / 2 for i in index])
ax1.set_xticklabels(regions)
ax1.legend()

# 在每个柱状图上显示具体数值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax1.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                '%d' % int(height), ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

# 创建第二个坐标轴
ax2 = ax1.twinx()

# 绘制折线图
line_color = 'g'
ax2.plot(index, completion_rates, color=line_color, linewidth=2, label='完成率')

# 设置第二个坐标轴属性
ax2.set_ylabel('完成率')
ax2.set_ylim([0, 110])
ax2.yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f%%'))
ax2.spines['right'].set_color(line_color)
ax2.yaxis.label.set_color(line_color)
ax2.tick_params(axis='y', colors=line_color)
ax2.legend(loc='upper center')

# 显示图形
plt.show()

from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

#创建两个实例
die_1 = Die()
die_2 = Die(10)
#掷几次骰子并将结果储存在一个列表中
results = []
for roll_num in range(5_0000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)#计算每种点数在results出现的次数
    frequencies.append(frequency)
print(frequencies)

#对结果进行可视化
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': '结果', 'dtick': 1}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='掷一个D6和一个D10的骰子 50000次的结果',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout':my_layout}, filename='d6_d10.html')
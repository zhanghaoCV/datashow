import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'D:/pythonproject/datashow/data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    # 从文件中获取日期和最高温度
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
# 根据最高气温绘制图形

plt.style.use('seaborn')

# 图形显示与模板的类型放在下列语句的位置会影响中文标签的显示
# plt.rcParams['font.sans-serif']=["SimHei"] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.rcParams['font.sans-serif'] = ["SimHei"]  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


# 设置图形的格式
title = '2018年每日最高温度和最低温度\n美国加利福尼亚死亡谷'
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()#倾斜x轴文字
ax.set_ylabel('温度（F）', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.show()

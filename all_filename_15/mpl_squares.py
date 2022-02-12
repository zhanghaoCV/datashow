import matplotlib.pyplot as plt

plt.style.use('seaborn')
#图形显示与模板的类型放在下列语句的位置会影响中文标签的显示
# plt.rcParams['font.sans-serif']=["SimHei"] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.rcParams['font.sans-serif']=["SimHei"] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
fig, ax = plt.subplots()
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10)
# ax.plot(squares, linewidth=3)#这个为单方面绘制squares图形
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0,1100,0,1100000])
plt.show()
#下面函数用来储存图片
#plt.savefig('squares_plot.png',bbox_inches='tight')
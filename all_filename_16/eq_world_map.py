import plotly.express as px
import json
import pandas as pd


#探索数据的结构
filename = 'd:/pythonproject/datashow/data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
mags, titles, lons, lats = [], [],[],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['经度','纬度','位置','震级']
)
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',#将前面的震级提供给它
    size_max=10,#标记最大尺寸为10像素点，默认为20像素点
    #使用了size，可以直观的看到随着震级增大，图上的原点也随之增大
    color='震级',
    hover_name='位置',
)
fig.write_html('global_earthquakes.html')
fig.show()#使用jupyternotebook可以直接打开
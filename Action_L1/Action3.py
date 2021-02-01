import pandas as pd
# 数据加载
df = pd.read_csv('./car_complain.csv')
# 数据预处理，拆分problem类型为多个字段
df = df.drop('problem', axis=1).join(df.problem.str.get_dummies(','))


def f(x):
    x = x.replace('一汽-大众', '一汽大众')
    return x


df['brand'] = df['brand'].apply(f)

# 数据统计
# 品牌投诉总数
result1 = df.groupby(['brand'])['id'].agg(['count'])
print('品牌投诉总数： \n' + str(result1))

# 车型投诉总数
result2 = df.groupby(['car_model'])['id'].agg(['count'])
print('车型投诉总数： \n' + str(result2))

# 平均车型投诉最多
temp1 = df.groupby(['brand', 'car_model'])['id'].agg(['count']).reset_index()
temp2 = temp1.groupby(['brand']).agg(
    {'car_model': 'count', 'count': 'sum'}).reset_index()
temp2['avg'] = temp2['count']/temp2['car_model']
result3 = temp2.sort_values(by='avg', ascending=False).reset_index()
print("平均车型投诉数最多的品牌是： %s, 其平均车型投诉数为： %d" %
      (result3.iloc[0]['brand'], result3.iloc[0]['avg']))

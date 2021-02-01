import pandas as pd
data = {'语文': [68, 95, 98, 90, 80], '数学': [
    65, 76, 86, 88, 90], '英语': [30, 98, 88, 77, 90]}
df = pd.DataFrame(data, index=['张飞', '关羽', '刘备', '典韦', '许诸'])
print(df)

# 统计这些人在语文，英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
result = [df.mean(), df.min(), df.max(), df.var(), df.std()]
print(pd.DataFrame(result, index=[
      '各科成绩均值', '各科成绩最小值', '各科成绩最大值', '各科成绩方差', '各科成绩标准差']))

# 统计每个人总成绩并输出
print('总成绩: \n'+str(df.sum(axis=1).sort_values(ascending=False)))

# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 20:53:18 2024

@author: 11794
"""

import pandas as pd

# 加载数据
file_path = 'REV5-data.xlsx'
df = pd.read_excel(file_path)

# 将字符串类型的datetime转换为Pandas的datetime类型
df['datetime'] = pd.to_datetime(df['datetime'])

# 假设数据包含四个方向的独热编码列
direction_columns = ['Direction_EB', 'Direction_NB', 'Direction_SB', 'Direction_WB']
for col in direction_columns:
    df.loc[df[col] == 1, 'Direction'] = col.replace('Direction_', '')

# 检查是否所有行都成功分配了方向
assert not df['Direction'].isnull().any(), "Some rows don't have a direction assigned."

# 删除不必要的列，只保留datetime, Direction 和 Vol
df = df[['datetime', 'Direction', 'Vol']]

# 按小时和方向分组，计算每组的总车流量
df_grouped = df.groupby([df['datetime'].dt.floor('H'), 'Direction'])['Vol'].sum().reset_index()

# 重命名列以提高清晰度
df_grouped.columns = ['datetime', 'direction', 'total_vol']

# 保存处理后的数据到新的Excel文件
output_file_path = 'REV5-data_1.xlsx'
df_grouped.to_excel(output_file_path, index=False)

print("数据处理完成，并已保存至:", output_file_path)

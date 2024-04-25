# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 00:44:13 2024

@author: 11794
"""

import pandas as pd

# 定义CSV文件路径
csv_file_path = 'Automated_Traffic_Volume_Counts_20240330.csv'  # 替换为你的CSV文件实际路径

# 读取CSV文件的前5000行
# 注意：根据你的文件大小和系统性能，这一步可能需要一些时间
df = pd.read_csv(csv_file_path, nrows=500000)

# 定义要导出的Excel文件路径
excel_file_path = 'ATVC_5.xlsx'  # 替换为你想要保存的Excel文件实际路径

# 将DataFrame导出到Excel文件，不包含索引
df.to_excel(excel_file_path, index=False)

print("CSV的前5000行已经成功导入到Excel文件中。")

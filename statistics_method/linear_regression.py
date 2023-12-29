import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv("sample.csv")

x = df['src15']  # x 軸欄位
y = df['src14']  # y 軸欄位

result = stats.linregress(x, y)

plt.scatter(x, y, color='black')
plt.axline(xy1=(0, result.intercept), slope=result.slope, linestyle="-", color="green")
plt.show()

print("截距", result.intercept)
print("斜率:", result.slope)
print("P-value:", result.pvalue)

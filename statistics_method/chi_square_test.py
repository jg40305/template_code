import pandas as pd
import scipy.stats as stats

df = pd.read_csv("chisquare.csv")

# 去除多餘資料
# df.drop(columns = ['產品', '訂單時間', '會員', '尺寸', '顏色'], inplace=True)
# 去除遺失值欄位
df.dropna()
# df = df.reset_index().drop(columns='index')

contingency_table = pd.crosstab(df['性別'], df['廣告'])
print(contingency_table)

observed = [[30, 10], [20, 15]]
chi2_stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)  # 卡方檢定

print(chi2_stat)
print(p_value)

import pandas as pd
import scipy.stats as stats

df = pd.read_csv("sample.csv")

t_statistic, p_value = stats.ttest_ind(df['src1'], df['src2'])  # 獨立樣本 t 檢定

# 顯示結果
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")
# 判斷結果是否顯著
alpha = 0.05
if p_value < alpha:
    print("結果顯著，拒絕虛無假設")
else:
    print("結果不顯著，無法拒絕虛無假設")


t_statistic, p_value = stats.ttest_rel(df['src1'], df['src2'])  # 成對樣本 t 檢定
alpha = 0.05
# 顯示結果
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")
# 判斷結果是否顯著
if p_value < alpha:
    print("結果顯著，拒絕虛無假設")
else:
    print("結果不顯著，無法拒絕虛無假設")


t_statistic, p_value = stats.ttest_1samp(df['src3'], 60)  # 單一樣本 t 檢定
alpha = 0.05
# 顯示結果
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")
# 判斷結果是否顯著
if p_value < alpha:
    print("結果顯著，拒絕虛無假設")
else:
    print("結果不顯著，無法拒絕虛無假設")


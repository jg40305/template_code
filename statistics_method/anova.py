import pandas as pd
import scipy.stats as stats
from scipy.stats import levene
from scipy.stats import f_oneway

df = pd.read_csv("sample.csv")

# 同質性檢定：不顯著需(p>.05)
statistic, p_value = levene(df["src1"], df["src2"], df["src3"])
print(f"statistic: {statistic}")
print(f"p_value: {p_value}")

if p_value < 0.05:
    # 單因子 ANOVA 檢定 顯著差異(p>.05)
    f_statistic, p_value = f_oneway(df["src1"], df["src2"], df["src3"])
    print(f"statistic: {f_statistic}")
    print(f"p_value: {p_value}")
else:
    print('同質性檢定未過')

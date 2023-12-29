import pandas as pd
import scipy.stats as stats

df = pd.read_csv("sample.csv")
pearson_coef, p_value = stats.pearsonr(df["src3"], df["src4"])

print(f"{pearson_coef}, {p_value}")
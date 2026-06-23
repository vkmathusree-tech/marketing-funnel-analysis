import pandas as pd

df = pd.read_csv("data.csv")

print("Marketing Funnel Analysis")
print(df)

df["Conversion_Rate"] = df["Users"].pct_change() * 100
print(df)

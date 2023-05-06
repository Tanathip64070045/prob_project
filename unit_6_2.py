import pandas as pd

df = pd.read_csv('dataset.csv')
df['Group 1'] = df[['JPY=X', 'THB=X', 'EUR=X', 'LKR=X', 'IQD=X']].mean(axis=1)
df['Date'] = pd.to_datetime(df['Date'])

df['Group 1'] = df[['JPY=X']].mean(axis=1)
df['Group 2'] = df[['THB=X']].mean(axis=1)
df['Group 3'] = df[['EUR=X']].mean(axis=1)
df['Group 4'] = df[['LKR=X']].mean(axis=1)
df['Group 5'] = df[['IQD=X']].mean(axis=1)

mean_group1 = df['Group 1'].mean()
mean_group2 = df['Group 2'].mean()
mean_group3 = df['Group 3'].mean()
mean_group4 = df['Group 4'].mean()
mean_group5 = df['Group 5'].mean()


print("Mean exchange rate for Japan:",mean_group1)
print("Mean exchange rate for Thailand:",mean_group2)
print("Mean exchange rate for Euro:",mean_group3)
print("Mean exchange rate for Sri Lanka:",mean_group4)
print("Mean exchange rate for Republic of Iraq:",mean_group5)
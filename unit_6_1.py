import pandas as pd

df = pd.read_csv('dataset.csv')
df['Date'] = pd.to_datetime(df['Date'])

df['Group 1'] = df[['JPY=X', 'THB=X', 'OMR=X', 'LKR=X', 'IQD=X']].mean(axis=1)
df['Group 2'] = df[['MYR=X', 'PHP=X', 'IDR=X', 'KRW=X', 'VND=X']].mean(axis=1)

mean_group1 = df['Group 1'].mean()
mean_group2 = df['Group 2'].mean()

diff_mean = mean_group1 - mean_group2

print(f'The difference in means between Group 1 and Group 2 is {diff_mean:.4f}')


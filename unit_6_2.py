import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
# อ่านข้อมูลจาก CSV
# สุ่มเลือก 5 ประเทศ

selected_currencies = ['IRR=X', 'THB=X', 'YER=X', 'JPY=X', 'PKR=X']
# อ่านข้อมูลจาก CSV
exchange_rates = pd.read_csv('dataset.csv')

# สุ่มเลือก 5 ประเทศ
countries = np.random.choice(selected_currencies.unique(), 5, replace=False)

# สร้าง DataFrame ที่เลือกเฉพาะประเทศที่สุ่มมา
selected_exchange_rates = exchange_rates[selected_currencies.isin(selected_currencies)]

# คำนวณค่าเฉลี่ยและส่วนเบี่ยงเบนมาตรฐานของแต่ละประเทศ
mean_rates = selected_exchange_rates.groupby('Date').mean()['Rate']
std_rates = selected_exchange_rates.groupby('Date').std()['Rate']

# คำนวณ z-score ของแต่ละวัน
selected_exchange_rates['z-score'] = (selected_exchange_rates['Rate'] - selected_exchange_rates.groupby('Country')['Rate'].transform('mean')) / selected_exchange_rates.groupby('Country')['Rate'].transform('std')

# สร้างการแจกแจงของค่าสัดส่วนตัวอย่าง
for country in selected_currencies:
    sns.histplot(data=selected_exchange_rates[selected_exchange_rates['Country'] == country], x='z-score', bins=30, kde=True, label=country)

plt.legend()
plt.show()

# คำนวณค่าเฉลี่ยของอัตราแลกเปลี่ยนดอลลาร์ในแต่ละประเทศ
for country in selected_currencies:
    print(f'Mean exchange rate for {country}: {mean_rates[country]:.4f}')
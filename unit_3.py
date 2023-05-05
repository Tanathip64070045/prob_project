import matplotlib.pyplot as plt
import pandas as pd

# อ่านข้อมูลจากไฟล์ CSV และนำเข้าเป็น DataFrame ของ Pandas
df = pd.read_csv('dataset.csv')

# แปลงคอลัมน์ 'Date' เป็น datetime
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

# ตั้งค่าคอลัมน์ 'Date' เป็น index ของ DataFrame
df.set_index('Date', inplace=True)

# กรองข้อมูลเฉพาะช่วงเวลาตั้งแต่ปี 2004 ถึงปี 2022
start_date = '1-1-2004'
end_date = '30-12-2022'
df = df.loc[start_date:end_date]

# สร้าง Series ของ Pandas ที่เก็บค่าเงิน THB ในแต่ละเดือน
thb_monthly_mean = df.groupby(pd.Grouper(freq='M'))['THB=X'].mean()

# สร้างกราฟเส้นของค่าเงิน THB ในแต่ละเดือน
ax = thb_monthly_mean.plot(figsize=(12, 6), title='Monthly Average of THB Exchange Rate (2004-2022)')
ax.set_xlabel('Year-Month')
ax.set_ylabel('THB per USD')
plt.show()
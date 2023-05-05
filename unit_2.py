import matplotlib.pyplot as plt
import pandas as pd

# อ่านข้อมูลจากไฟล์ CSV และนำเข้าเป็น DataFrame ของ Pandas
df = pd.read_csv('dataset.csv')

# แปลงคอลัมน์ 'Date' เป็น datetime
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

# ตั้งค่าคอลัมน์ 'Date' เป็น index ของ DataFrame
df.set_index('Date', inplace=True)

start_date = '1-1-2004'
end_date = '30-12-2004'

# คำนวณค่าความแปรปวนของสกุลเงินแต่ละปี
thb_var_by_year = df.groupby(df.index.year)['THB=X'].var()

# สร้างกราฟความแปรปวนของสกุลเงินแต่ละปี
ax = thb_var_by_year.plot(kind='bar', x='Year', y='Variance', figsize=(10,6))
ax.set_xlabel('Year')
ax.set_ylabel('Variance')
ax.set_title('Variation of THB Exchange Rate by Year')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

### ตัวอย่างโจทย์: วิเคราะห์ความถดถอยของสกุลเงินต่างๆ เมื่อเทียบกับสกุล Thai Baht คุณสามารถทำตามขั้นตอนดังนี้:

# อ่านข้อมูลจากไฟล์ CSV
df = pd.read_csv('dataset.csv')

# เพิ่มค่าเงิน USD
df['USD=X'] = 1.0

# ตั้งคอลัมน์ 'Date' เป็น index
df.set_index('Date', inplace=True)

# กรองข้อมูลตามวันที่ที่กำหนด
start_date = '1-1-2004'
end_date = '30-12-2022'
df = df.loc[(df.index >= start_date) & (df.index <= end_date)]

# drop ข้อมูลที่เป็น null
df.dropna(inplace=True)

# ฟังก์ชั่นสำหรับวาดกราฟและคำนวณค่าถดถอย
def plot_regression(df, x_col, y_col):
    # สร้างกราฟ scatter plot
    plt.scatter(df[x_col], df[y_col])

    # คำนวณค่า slope และ intercept ของเส้น regression
    slope, intercept = np.polyfit(df[x_col], df[y_col], 1)

    # สร้างเส้น regression และเพิ่มเข้าไปในกราฟ
    plt.plot(df[x_col], slope * df[x_col] + intercept, color='red')

    # แสดงค่า slope และ intercept
    print(f'Slope: {slope:.2f}, Intercept: {intercept:.2f}')

# สร้าง figure ขนาด 16x8 นิ้ว
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(16, 8))

# วาดกราฟสกุลเงิน EUR
plt.subplot(2, 2, 1)
plot_regression(df, 'THB=X', 'EUR=X')
plt.title('EUR')

# วาดกราฟสกุลเงิน MYR
plt.subplot(2, 2, 2)
plot_regression(df, 'THB=X', 'MYR=X')
plt.title('MYR')

# วาดกราฟสกุลเงิน JPY
plt.subplot(2, 2, 3)
plot_regression(df, 'THB=X', 'JPY=X')
plt.title('JPY')

plt.subplot(2, 2, 4)
plot_regression(df, 'THB=X', 'CNY=X')
plt.title('CNY')

# แสดงกราฟทั้งหมด
plt.show()

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

print('นักเศรษฐศาสตร์ต้องการศึกษาการแจกแจงค่าสัดส่วนตัวอย่างของอัตราแลกเปลี่ยนดอลลาร์ระหว่างประเทศในเอเชีย ข้อมูลประกอบด้วย 18 ประเทศในเอเชีย ตั้งแต่วันที่ 1 มกราคม 2010 ถึง 31 ธันวาคม 2010 สุ่มเลือกห้าประเทศจาก dataset และคำนวณ z-score ของอัตราแลกเปลี่ยนดอลลาร์ในแต่ละวัน จากนั้นสร้างการแจกแจงของค่าสัดส่วนตัวอย่าง จงหาความน่าจะเป็นค่าเฉลี่ยของอัตราแลกเปลี่ยนดอลลาร์ในแต่ละประเทศ 5 ประเทศที่สุ่มมา')

print("Mean exchange rate for Japan:",mean_group1)
print("Mean exchange rate for Thailand:",mean_group2)
print("Mean exchange rate for Euro:",mean_group3)
print("Mean exchange rate for Sri Lanka:",mean_group4)
print("Mean exchange rate for Republic of Iraq:",mean_group5)
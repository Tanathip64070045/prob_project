import pandas as pd



df = pd.read_csv('dataset.csv')
df['Date'] = pd.to_datetime(df['Date'])

df['Group 1'] = df[['JPY=X', 'THB=X', 'OMR=X', 'LKR=X', 'IQD=X']].mean(axis=1)
df['Group 2'] = df[['MYR=X', 'PHP=X', 'IDR=X', 'KRW=X', 'VND=X']].mean(axis=1)

mean_group1 = df['Group 1'].mean()
mean_group2 = df['Group 2'].mean()

diff_mean = mean_group1 - mean_group2
print('นักเศรษฐศาสตร์ต้องการหาว่าอัตราแลกเปลี่ยนดอลลาร์ระหว่างกลุ่มที่ 1 และกลุ่มที่ 2 มีค่าเฉลี่ยต่างกันมากน้อยแค่ไหน โดยใช้ข้อมูลอัตราแลกเปลี่ยนดอลลาร์ในแต่ละประเทศในแต่ละวันของแต่ละกลุ่ม ในช่วงเวลาที่กำหนด ข้อมูลประกอบด้วยอัตราแลกเปลี่ยนดอลลาร์ในประเทศต่างๆของเอเชียตั้งแต่วันที่ 1 มกราคม 2010 ถึง 31 ธันวาคม 2010 โดยแบ่งเป็น 2 กลุ่ม ดังนี้ กลุ่มที่ 1: ญี่ปุ่น (JPY), ฮ่องกง (HKD), สิงคโปร์ (SGD), ไต้หวัน (TWD), เกาหลีใต้ (KRW)กลุ่มที่ 2: มาเลเซีย (MYR), ฟิลิปปินส์ (PHP), อินโดนีเซีย (IDR), กัมพูชา (KHR), เวียดนาม (VND)')
print(f'The difference in means between Group 1 and Group 2 is {diff_mean:.4f}')




# success
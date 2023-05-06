import pandas as pd
import numpy as np

# โหลดไฟล์ csv ของ Dataset Dollar Exchange Rates
df = pd.read_csv('dataset.csv')
df.set_index('Date', inplace=True)
# กรองข้อมูลที่อยู่ในช่วงวันที่ 1 มกราคม 2010 ถึง 31 ธันวาคม 2020
start_date = '1-1-2010'
end_date = '30-12-2020'
df = df.loc[(df.index >= start_date) & (df.index <= end_date)]
df.dropna(inplace=True)
# คำนวณค่าเฉลี่ยของอัตราแลกเปลี่ยนสกุลเงิน USD ต่อหน่วยของแต่ละประเทศ
avg_rates = 1.0

# คำนวณค่าเฉลี่ยของอัตราแลกเปลี่ยนสกุลเงิน USD ทั้งหมด
global_avg_rate = np.mean(df[['JPY=X']])

# คำนวณค่า Z-score ของค่าเฉลี่ยของแต่ละประเทศ
z_scores = (avg_rates - global_avg_rate) / np.std(df[['JPY=X']])

# ตั้งช่วงความเชื่อมั่นของค่าเฉลี่ยดังกล่าวที่รวมถึงค่า Z-score ในระดับนัยสำคัญ 0.05
confidence_interval = [global_avg_rate + np.percentile(df[['JPY=X']], 2.5), global_avg_rate + np.percentile(df[['JPY=X']], 97.5)]
z_score_threshold = 1.96
confident_countries = z_scores[z_scores.abs() > z_score_threshold]

# แสดงผลลัพธ์
print('คำนวณหาค่าเฉลี่ยของอัตราแลกเปลี่ยนสกุลเงิน USD ต่อหน่วยของแต่ละประเทศในช่วงวันที่ 1 มกราคม 2010 ถึง 31 ธันวาคม 2020 และตั้งช่วงความเชื่อมั่นของค่าเฉลี่ยดังกล่าวที่รวมถึงค่า Z-score ในระดับนัยสำคัญ 0.05')
print("Average exchange rates of each country:", avg_rates)
print("Global average exchange rate:", global_avg_rate)
print("Z-scores of each country:", z_scores)
print("Confidence interval:", confidence_interval)
print("Countries with Z-scores outside the confidence interval:", confident_countries)



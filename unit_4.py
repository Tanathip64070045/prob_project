import pandas as pd
from scipy.stats import binom

import numpy as np
import matplotlib.pyplot as plt


test = []
df = pd.read_csv('dataset.csv')
for index, row in df.iterrows():
    if str(row['THB=X']) != "nan":
        test.append(row['THB=X'])


# ตัวอย่างโจทย์: สมมุติว่าคุณได้รับข้อมูลอัตราแลกเปลี่ยนระหว่างสกุลเงินบาท (THB) และดอลลาร์สหรัฐ (USD) ในรูปแบบ CSV ในระยะเวลาหนึ่ง จงทำการวิเคราะห์ความน่าจะเป็นของการมีค่าอัตราแลกเปลี่ยน THB/USD เพิ่มขึ้นหรือลดลงในแต่ละวัน โดยใช้การแจกแจงแบบ binomial และพล็อตกราฟดังกล่าวด้วย Python

# ขั้นตอนที่ควรทำคือ:

# อ่านข้อมูล CSV ที่มีค่าอัตราแลกเปลี่ยน THB/USD ในแต่ละวัน
# คำนวณความน่าจะเป็นของการมีค่าอัตราแลกเปลี่ยน THB/USD เพิ่มขึ้นหรือลดลงในแต่ละวัน
# ทำการวิเคราะห์ความน่าจะเป็นด้วยการแจกแจงแบบ binomial
# พล็อตกราฟความน่าจะเป็นแบบ binomial ของการมีค่าอัตราแลกเปลี่ยน THB/USD เพิ่มขึ้นหรือลดลงในแต่ละวัน
# ตัวอย่างโค้ด Python:

# 1. อ่านข้อมูล CSV
exchange_rates = test
# 2. คำนวณความน่าจะเป็นของการมีค่าอัตราแลกเปลี่ยน THB/USD เพิ่มขึ้นหรือลดลงในแต่ละวัน
rate_changes = np.diff(exchange_rates)
rate_increases = np.sum(rate_changes > 0)
total_days = len(rate_changes)

# 3. วิเคราะห์ความน่าจะเป็นด้วยการแจกแจงแบบ binomial
p_increases = rate_increases / total_days
binom_dist = binom(total_days, p_increases)

# 4. พล็อตกราฟความน่าจะเป็นแบบ binomial ของการมีค่าอัตราแลกเปลี่ยน THB/USD เพิ่มขึ้นหรือลดลงในแต่ละวัน
x = np.arange(0, total_days + 1)
pmf = binom_dist.pmf(x)

plt.vlines(x, 0, pmf, colors='b', lw=5, alpha=0.5)
plt.plot(x, pmf, 'bo', ms=8, alpha=0.5)
plt.xlabel('Number of Days with Increased Exchange Rate')
plt.ylabel('Probability')
plt.title('Binomial Distribution of Increased THB/USD Exchange Rates')
plt.show()

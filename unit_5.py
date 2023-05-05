import pandas as pd
from scipy.stats import norm

import numpy as np
import matplotlib.pyplot as plt

# 1. อ่านข้อมูล CSV

test = []
df = pd.read_csv('dataset.csv')
for index, row in df.iterrows():
    if str(row['THB=X']) != "nan":
        test.append(row['THB=X'])

# ในการวิเคราะห์ความน่าจะเป็นแบบต่อเนื่องสำหรับสกุลเงิน THB/USD ด้วยการแจกแจงแบบ normal distribution (การแจกแจงปกติ) คุณสามารถทำตามขั้นตอนดังนี้:

# อ่านข้อมูล CSV ที่มีค่าอัตราแลกเปลี่ยนสกุลเงิน THB/USD ในแต่ละวัน
# คำนวณค่าเฉลี่ย (mean) และค่าความแปรปรวน (variance) ของข้อมูลอัตราแลกเปลี่ยน
# พล็อตกราฟความน่าจะเป็นของการแจกแจงแบบ normal distribution ตามค่าเฉลี่ยและค่าความแปรปรวนที่คำนวณได้

exchange_rates = test

# 2. คำนวณค่าเฉลี่ยและค่าความแปรปรวนของข้อมูลอัตราแลกเปลี่ยน
mean = np.mean(exchange_rates)
std_dev = np.std(exchange_rates)

# 3. พล็อตกราฟความน่าจะเป็นของการแจกแจงแบบ normal distribution
x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 1000)
pdf = norm.pdf(x, mean, std_dev)

plt.plot(x, pdf)
plt.xlabel('Exchange Rate THB/USD')
plt.ylabel('Probability Density')
plt.title('Normal Distribution of THB/USD Exchange Rates')
plt.show()
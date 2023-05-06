
import pandas as pd
import numpy as np
from scipy.stats import t

# อ่านข้อมูลจากไฟล์ CSV ของ Dataset Dollar Exchange Rates
df = pd.read_csv("dataset.csv")

# สุ่มเลือกข้อมูลอัตราแลกเปลี่ยนสกุลเงินระหว่างประเทศเอเชียและยุโรป
asia_rates = df[['PHP=X']]
europe_rates = df[['EUR=X']]
df.dropna(inplace=True)
# คำนวณค่าผลต่างระหว่างค่าเฉลี่ยของสองกลุ่ม
mean_diff = np.mean(asia_rates) - np.mean(europe_rates)

# คำนวณค่า t-score และค่า p-value โดยใช้ t-distribution
n1 = len(asia_rates)
n2 = len(europe_rates)
s1 = np.std(asia_rates, ddof=1)
s2 = np.std(europe_rates, ddof=1)
se =( (s1**2 /n1) + 1) **-1
t_score = mean_diff / se
p_value = 2 * (1 - t.cdf(abs(t_score), n1+n2-2))

# คำนวณค่าความเชื่อมั่นด้วย t-distribution
alpha = 0.05
t_critical = t.ppf(1 - alpha/2, n1+n2-2)
margin_of_error = t_critical * se
confidence_interval = (mean_diff - margin_of_error, mean_diff + margin_of_error)

print('ในการศึกษาความแตกต่างของอัตราแลกเปลี่ยนสกุลเงินระหว่างประเทศสองกลุ่ม คุณได้สุ่มเลือกตัวอย่างของสองกลุ่ม คือกลุ่มประเทศเอเชียและกลุ่มประเทศยุโรป จงคำนวณค่าผลต่างระหว่างค่าเฉลี่ยของสองกลุ่ม และตั้งช่วงความเชื่อมั่นของผลต่างระหว่างค่าเฉลี่ยของสองกลุ่มที่รวมถึงค่า Z-score ในระดับนัยสำคัญ 0.05 และใช้วิธีการแจกแจงตัวอย่างสองกลุ่มแบบการแจกแจง t (t-distribution) ของสถิติ')

print("Mean Difference:", mean_diff)
print("t-score:", t_score)
print("p-value:", p_value)
print("Confidence Interval:", confidence_interval)


